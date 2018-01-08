from pprint import pprint
from pymongo import MongoClient
from bson import ObjectId
from config import app_cfg
from logger import logger

DATATBASE_NAME = app_cfg[('DATABASE', 'name')]

class DataConnector(object):

    def __init__(self, collection_name):
        client = MongoClient(connect=False)
        db = client[DATATBASE_NAME]
        self.collection = db[collection_name]

    def __iter__(self):
        return (item for item in self.collection.find())

    def __getitem__(self, _id):
        return self.collection.find_one({'_id': ObjectId(_id)})

    def __add__(self, data):
        return self.collection.insert(data)

    def __sub__(self, _id):
        self.collection.find({'_id': ObjectId(_id)})
        self.collection.remove({'_id': ObjectId(_id)})
        self.collection.find({'_id': ObjectId(_id)})

    def __iadd__(self, udpate_info):
        _id, data = udpate_info
        self.collection.replace_one({'_id': ObjectId(_id)}, data)
        return self

    def clear(self):
        for document in self:
            self - document[_id]
        return list(self)

    def get_by_name(self, name):
        for item in self:
            if name in item.values():
                return item

if __name__ == '__main__':
    dc = DataConnector('users')
    # pprint(list(dc))
    dc.clear()
