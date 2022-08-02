import scrapy

from ..items import WebcrawlerItem


class QuotesSpider(scrapy.Spider):
    name = "webcrawler"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for quote in response.css('div.quote'):
            item = WebcrawlerItem()         

            item['title'] = quote.css('span.text::text').get()
            item['author'] = {
                'name': quote.css('small.author::text').get(),
                'url':quote.xpath('//span/a/@href').get()
            }
            item['tag'] =  quote.css('div.tags a.tag::text').getall()
            
            yield item
    
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
        