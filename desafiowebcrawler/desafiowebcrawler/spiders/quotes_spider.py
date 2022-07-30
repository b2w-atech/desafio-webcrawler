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

    def start(self, response):
        #### Abre a requisicao no navegador (bom para visualizar funcionamento)
        #open_in_browser(response)
        
        #### Inicia o scraping ####
        itens = DesafiowebcrawlerItem()

        all_div_quotes = response.css("div.quote")
        
        for div in all_div_quotes:
            title = div.css('span.text::text').extract()
            author = {
                'name': div.css('.author::text').extract(),
                'link_bio': div.css('.author::attr(href)').extract(),
            }
            tag = div.css('.tag::text').extract()
            
            itens['title'] = title
            itens['author'] = author
            itens['tag'] = tag

            yield itens

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:

            yield response.follow(next_page, callback= self.start)