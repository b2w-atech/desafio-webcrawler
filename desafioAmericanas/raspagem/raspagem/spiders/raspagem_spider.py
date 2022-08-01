import scrapy


class RaspagemSpiderSpider(scrapy.Spider):
    name = 'raspagem_spider'
    start_urls = ['http://quotes.toscrape.com/']

    # def start_requests(self):
    #     urls = ['http://quotes.toscrape.com/']
        
    # for url in urls:
    #     yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response, **kwargs):
        # tags = []
        # listaAutor = []
        for i in response.xpath('//div[@class="quote"]'):
            citacao = i.xpath('.//span[@class="text"]//text()').get()
            nome = i.xpath('.//small[@class="author"]//text()').get()
            url = i.xpath('.//span/a/@href').get()
    
            tags = [resultado for resultado in i.xpath('.//div[@class="tags"]//text()')[1:-1].getall() if resultado.strip()]

            autor = {
                'nome': nome,
                'url': url
            }
            # listaAutor.append(autor) 
           

            yield {
                'citacao': citacao,
                'autor': autor,
                # 'nome': nome,
                # 'url': url,
                'tags': tags
            }
        
        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        proxima_pagina = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if proxima_pagina:
            yield scrapy.Request(
                response.urljoin(proxima_pagina),
                callback=self.parse
            )