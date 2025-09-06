from fastapi import FastAPI
from typing import Dict, Optional
from mongo_dal import MongoDAL
from elastic_dal import ElasticDAL

app = FastAPI(title="Unified Mongo + Elastic API")

# חיבורים למסדים
mongo = MongoDAL(db_name="test_db", collection_name="test_collection")
elastic = ElasticDAL(index_name="test_index")

# --- CRUD פשוט --- #

# יצירת מסמך
@app.post("/create/")
def create_document(data: Dict, db_type: str, id: Optional[str] = None):
    if db_type == "mongo":
        inserted_id = mongo.insert_one(data)
        result = {"inserted_id": inserted_id}
    elif db_type == "elastic":
        doc_id = id or "1"
        elastic.insert_document(doc_id, data)
        result = {"inserted_id": doc_id}
    else:
        result = {"error": "Unknown db_type"}
    return result

# קריאת מסמכים
@app.get("/read/")
def read_documents(query: Dict = {}, db_type: str = "mongo"):
    if db_type == "mongo":
        documents = mongo.find_many(query)
        result = {"documents": documents}
    elif db_type == "elastic":
        documents = elastic.search_documents(query)
        result = {"documents": documents}
    else:
        result = {"error": "Unknown db_type"}
    return result

# עדכון מסמך
@app.put("/update/{id}")
def update_document(id: str, data: Dict, db_type: str):
    if db_type == "mongo":
        updated_count = mongo.update_one({"_id": id}, data)
        result = {"updated_count": updated_count}
    elif db_type == "elastic":
        elastic.update_document(id, data)
        result = {"updated_id": id}
    else:
        result = {"error": "Unknown db_type"}
    return result

# מחיקת מסמך
@app.delete("/delete/{id}")
def delete_document(id: str, db_type: str):
    if db_type == "mongo":
        deleted_count = mongo.delete_one({"_id": id})
        result = {"deleted_count": deleted_count}
    elif db_type == "elastic":
        elastic.delete_document(id)
        result = {"deleted_id": id}
    else:
        result = {"error": "Unknown db_type"}
    return result
