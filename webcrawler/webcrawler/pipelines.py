# Define your item pipelines here
import pymongo

from itemadapter import ItemAdapter


class WebcrawlerPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient(
                'localhost', 27017
        )

        self.db = self.conn['quotestoscrape']
        self.collection = self.db['luana_scardua']
    
        if 'quotestoscrape' in self.conn.list_database_names():
            self.collection.drop()
            
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
