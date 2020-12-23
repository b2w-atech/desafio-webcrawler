import scrapy
from ..items import QuotesProjectItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'

    base_url = 'http://quotes.toscrape.com'
    author = {'name': '', 'url': ''}

    start_urls = [
        base_url,
    ]

    def parse(self, response):
        div_collection = response.css('div.quote')

        items = QuotesProjectItem()

        for quote in div_collection:
            title = quote.css('span.text::text').extract_first()
            author_name = quote.css('.author::text').extract_first()
            author_url = quote.xpath('//span//@href').extract_first()
            self.author['name'], self.author['url'] = (
                author_name,
                self.base_url + author_url,
            )
            # self.author['url'] = author_url
            tags = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = self.author
            items['tags'] = tags

            yield items

        next = response.css('li.next a::attr(href)').get()

        if next:
            yield response.follow(next, callback=self.parse)
