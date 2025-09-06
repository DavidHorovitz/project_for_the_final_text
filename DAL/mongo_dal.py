# mongo_dal.py
from pymongo import MongoClient
# from bson.objectid import ObjectId
import os


class MongoDAL:
    def __init__(self, db_name="mydb", collection_name="mycollection"):
        self.mongo_user = os.getenv("MONGO_USER", "root")
        self.mongo_pass = os.getenv("MONGO_PASS", "example")
        self.mongo_host = os.getenv("MONGO_HOST", "localhost")
        self.mongo_port = int(os.getenv("MONGO_PORT", 27017))

        self.client = MongoClient(
            host=self.mongo_host,
            port=self.mongo_port,
            username=self.mongo_user,
            password=self.mongo_pass
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, data: dict):
        """Insert a single document into the collection"""
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def insert_many(self, data_list: list):
        """Insert multiple documents"""
        result = self.collection.insert_many(data_list)
        return [str(_id) for _id in result.inserted_ids]

    def find_one(self, query: dict):
        """Find a single document matching the query"""
        return self.collection.find_one(query)

    def find_many(self, query: dict, skip=0, limit=100):
        """Find multiple documents with pagination"""
        cursor = self.collection.find(query).skip(skip).limit(limit)
        return list(cursor)

    def update_one(self, query: dict, update_data: dict):
        """Update a single document"""
        result = self.collection.update_one(query, {"$set": update_data})
        return result.modified_count

    def delete_one(self, query: dict):
        """Delete a single document"""
        result = self.collection.delete_one(query)
        return result.deleted_count

    def count_documents(self, query: dict = {}):
        """Count documents matching query"""
        return self.collection.count_documents(query)
