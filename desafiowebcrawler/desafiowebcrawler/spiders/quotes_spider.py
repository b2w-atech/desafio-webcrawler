from gc import callbacks
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import DesafiowebcrawlerItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    #### Faz login na pagina
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(
            response,
            formdata={
                'csrf_token': token,
                'username': 'teste',
                'password': 'teste'
            },
            callback=self.start
        )

    #### Inicia a coleta de dados ####
    def start(self, response):
        #### open_in_browser(response) abre a requisicao no navegador (bom para visualizar funcionamento)
        url = 'https://quotes.toscrape.com{}'
        itens = DesafiowebcrawlerItem()
        # Aloca todas as divs em uma variavel
        all_div_quotes = response.css("div.quote")
        
        # Percorre as divs iterando sobre os dados , a pipe armazena no banco
        for div in all_div_quotes:
            title = div.css('span.text::text').extract_first()
            author = {
                'name': div.css('.author::text').extract_first(),
                'url': url.format(div.xpath(
                '/html/body/div/div[2]/div[1]/div[1]/span[2]/a/@href'
                ).extract_first())
            }
            tag = div.css('.tag::text').extract()
            
            itens['title'] = title
            itens['author'] = author
            itens['tag'] = tag

            yield itens

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:

            yield response.follow(next_page, callback= self.start)