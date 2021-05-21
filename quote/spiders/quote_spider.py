import scrapy

from scrapy.selector import Selector

from quote.items import QuoteItem

class QuoteSpider(scrapy.Spider):
    name = "quote"

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com']

    def parse(self, response):
        base_url = 'https://quotes.toscrape.com'
        quotes = Selector(response).xpath('//div[@class="quote"]')

        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.xpath('.//span[@class="text"]/text()').get()
            item['author'] = {
                'name': quote.xpath('.//small[@class="author"]/text()').get(),
                'bio': base_url + quote.xpath('.//a[contains(@href, "author")]/@href').get(),
                }
            item['tags'] = quote.xpath('.//a[contains(@class, "tag")]/text()').getall()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)

