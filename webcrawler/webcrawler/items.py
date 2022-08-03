# Define here the models for your scraped items

import scrapy


class WebcrawlerItem(scrapy.Item):
    
    author = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()
    