from fastapi import FastAPI
from typing import Dict, Optional
from DAL.elastic_dal import ElasticDAL
import uvicorn
app = FastAPI(title="Elasticsearch Simple API")

# מחובר ל־Elasticsearch
elastic = ElasticDAL(index_name="test_index")

# --- CRUD פשוט ---

# יצירת מסמך חדש
@app.post("/elastic")
def create_elastic(data: Dict, id: Optional[str] = None):
    doc_id = id or "1"  # אם אין id, נשתמש ב־"1"
    elastic.insert_document(doc_id, data)  # שמירה באלסטיק
    result = {"inserted_id": doc_id}  # הכנת התוצאה
    return result

# קריאה של מסמכים לפי query פשוט
@app.get("/elastic")
def read_elastic(query: Dict = {}):
    documents = elastic.search_documents(query)  # חיפוש במסד
    result = {"documents": documents}  # הכנת התוצאה
    return result

# עדכון מסמך לפי ID
@app.put("/elastic/{id}")
def update_elastic(id: str, data: Dict):
    elastic.update_document(id, data)  # עדכון במסד
    result = {"updated_id": id}  # הכנת התוצאה
    return result

# מחיקת מסמך לפי ID
@app.delete("/elastic/{id}")
def delete_elastic(id: str):
    elastic.delete_document(id)  # מחיקה במסד
    result = {"deleted_id": id}  # הכנת התוצאה
    return result
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')