import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()

            item['title'] = quote.css('span.text::text').get()
            item['author'] = {
                'name': quote.css('small.author::text').get(),
                'url': 'http://quotes.toscrape.com' + quote.css('span a::attr(href)').extract()[0],
            }
            item['tags'] = quote.css('div.tags a.tag::text').getall()

            yield item


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
