# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import attrs


@attr.s
class QuoteItem:
    title: str = attr.ib(default='')
    author: dict = attr.ib(default={'name': '', 'url': ''})
    tags: list = attr.ib(default=[])
