from scrapy.item import Item, Field


class QuoteItem(Item):
    text = Field()
    author = Field()
    tags = Field()