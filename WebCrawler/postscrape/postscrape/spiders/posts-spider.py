import scrapy
from ..items import PostscrapeItem

class TitleSpider(scrapy.Spider):
    name = "titles"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):

        itens = PostscrapeItem()

        div_titles = response.css('div.quote')

        for title in div_titles:
                text = title.css('span.text::text').get()
                author = title.css('span small::text').get()
                link = title.css('span a::attr(href)').get()
                tag = title.css('div.tags a.tag::text').getall()

                itens['text'] = text
                itens['author'] = {'name': author ,
                                    'url':'http://quotes.toscrape.com'+link}
                itens['tag'] = tag

                yield itens

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    

        
        """
        page = response.url.split('/')[-1]
        filename = 'posts-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)


            class titlesSpider(scrapy.Spider):
   
        """