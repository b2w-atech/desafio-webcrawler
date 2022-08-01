import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1', 'http://quotes.toscrape.com/page/2']
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        pagina = response.url.split("/")[-2]
        nome_arquivo = f'quotes-{page}.html'
        with open(nome_arquivo, 'wb') as f:
            f.write(response.body)
        
        self.log('Arquivo salvo {}'.format(nome_arquivo))
