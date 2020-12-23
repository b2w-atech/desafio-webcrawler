import scrapy


class QuotesProjectItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
