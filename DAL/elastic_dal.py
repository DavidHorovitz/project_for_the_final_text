# elastic_dal.py
from elasticsearch import Elasticsearch
import os

class ElasticDAL:
    def __init__(self, index_name="my_index"):
        self.es_host = os.getenv("ELASTIC_HOST", "http://localhost:9200")
        self.index_name = index_name
        self.es = Elasticsearch(self.es_host)

    def insert_document(self, doc_id: str, data: dict):
        """Insert or update a document"""
        return self.es.index(index=self.index_name, id=doc_id, document=data)

    def get_document(self, doc_id: str):
        """Get a document by ID"""
        try:
            return self.es.get(index=self.index_name, id=doc_id)['_source']
        except:
            return None

    def search_documents(self, query: dict, size=100):
        """Search documents with a query"""
        result = self.es.search(index=self.index_name, query=query, size=size)
        return [hit["_source"] for hit in result["hits"]["hits"]]

    def update_document(self, doc_id: str, update_data: dict):
        """Update a document by ID"""
        body = {"doc": update_data}
        return self.es.update(index=self.index_name, id=doc_id, body=body)

    # elastic = ElasticDAL("students")
    #
    # # הכנסת מסמך
    # elastic.insert_document("1", {"name": "David", "age": 25, "city": "Tel Aviv"})
    # elastic.update_document("1", {"age": 26})
    # {
    #     "name": "David",
    #     "age": 26,
    #     "city": "Tel Aviv"
    # }
    # elastic.update_document("1", {"grade": "A"})
    # {
    #     "name": "David",
    #     "age": 26,
    #     "city": "Tel Aviv",
    #     "grade": "A"
    # }

    def delete_document(self, doc_id: str):
        """Delete a document by ID"""
        return self.es.delete(index=self.index_name, id=doc_id)
