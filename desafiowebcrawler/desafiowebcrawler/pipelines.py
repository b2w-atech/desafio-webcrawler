# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class DesafiowebcrawlerPipeline(object):

    def __init__(self):
        ## Conectando no mongodb
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        ## Criando o banco
        db = self.conn['quotestoscrape']
        ## Criando a tabela
        self.collection = db['matheus_ferreira']
        #### Dropei a collection para nao duplicar os dados caso rode o scrapy duas vezes na mesma pagina
        self.collection.drop()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
