import scrapy
from desafio_webcrawler.items import DesafioWebcrawlerItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):

            title = quote.xpath('./span[@class="text"]/text()').extract_first()
            author_name = quote.xpath('.//small[@class="author"]/text()').extract_first()
            author_url = self.start_urls[0]+quote.xpath('.//a[1]/@href').extract_first()
            tags = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            author = {
                "name":author_name,
                "url": author_url
            }
            yield DesafioWebcrawlerItem(title=title, author=author, tags=tags)
                    
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
