# Define here the models for your scraped items

import scrapy


class WebcrawlerItem(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()
    tag = scrapy.Field()
    