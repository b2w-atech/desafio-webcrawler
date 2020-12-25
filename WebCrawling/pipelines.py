import pymongo

MONGO_URL = 'mongodb+srv://admin:quotescrape@cluster0.lw17c.mongodb.net/quotescrape?retryWrites=true&w=majority'
MONGO_DB = 'quotescrape'
DB_COLLECTION = 'marcosvinicius_simoescampos'


class WebcrawlingPipeline:

    def __init__(self):
        self.connection = pymongo.MongoClient(MONGO_URL)
        DATABASE = self.connection[MONGO_DB]
        self.collection = DATABASE[DB_COLLECTION]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
