import scrapy
from WebCrawling.models.items import WebcrawlingItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            title = quote.css('span.text::text').get()
            author = {
                'name': quote.css('small.author::text').get(),
                'url': 'http://quotes.toscrape.com' + quote.css('span a::attr(href)').get()
            }
            tags = quote.css('div.tags a.tag::text').getall()

            items = WebcrawlingItem()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
