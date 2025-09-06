from fastapi import FastAPI
from typing import Dict
from mongo_dal import MongoDAL

app = FastAPI(title="MongoDB Simple API")

# מחובר למסד MongoDB
mongo = MongoDAL(db_name="test_db", collection_name="test_collection")

# --- CRUD פשוט ---

# יצירת מסמך חדש
@app.post("/mongo/")
def create_mongo(data: Dict):
    inserted_id = mongo.insert_one(data)  # שמירה במסד
    result = {"inserted_id": inserted_id}  # הכנת התוצאה
    return result  # החזרת התוצאה למשתמש

# קריאה של כל המסמכים
@app.get("/mongo/")
def read_mongo():
    documents = mongo.find_many({})  # קריאה מכל המסמכים
    result = {"documents": documents}  # הכנת התוצאה
    return result

# עדכון מסמך לפי ID
@app.put("/mongo/{id}")
def update_mongo(id: str, data: Dict):
    updated_count = mongo.update_one({"_id": id}, data)  # עדכון במסד
    result = {"updated_count": updated_count}  # הכנת התוצאה
    return result

# מחיקת מסמך לפי ID
@app.delete("/mongo/{id}")
def delete_mongo(id: str):
    deleted_count = mongo.delete_one({"_id": id})  # מחיקה במסד
    result = {"deleted_count": deleted_count}  # הכנת התוצאה
    return result
