# main.py
from mongo_dal import MongoDAL
from elastic_dal import ElasticDAL

# MongoDB
mongo = MongoDAL(db_name="test_db", collection_name="test_collection")
mongo.insert_one({"name": "David", "age": 36})
print(mongo.find_many({}))

# Elasticsearch
es = ElasticDAL(index_name="test_index")
es.insert_document(doc_id="1", data={"name": "David", "age": 36})
print(es.get_document("1"))



# דוגמאות
mongo.find_many({"name": "David"})  # מחזיר מסמכים עם שם = David

mongo.find_many({"age": {"$gt": 30}})  # גיל > 30

mongo.find_many({
    "$and": [
        {"age": {"$gt": 20}},
        {"name": {"$regex": "^D"}}  # שם שמתחיל ב־D
    ]
})

# $eq	שווה ל־value
# $ne	לא שווה ל־value
# $gt	גדול מ־value
# $gte	גדול או שווה ל־value
# $lt	קטן מ־value
# $lte	קטן או שווה ל־value
# $in	שווה לאחד מהערכים במערך
# $nin	לא שווה לאף ערך במערך
# $and, $or, $not	שילוב תנאים

# דוגמה בסיסית של חיפוש
query = {
    "match": {"name": "David"}
}
es.search_documents(query)

# חיפוש עם תנאי
query = {
    "bool": {
        "must": [
            {"range": {"age": {"gt": 30}}},  # גיל > 30
            {"match": {"name": "David"}}    # שם = David
        ]
    }
}
es.search_documents(query)

# match	{"match": {"field": "value"}}	חיפוש טקסטואלי
# term	{"term": {"field": "value"}}	חיפוש מדויק
# range	{"range": {"field": {"gt": 5}}}	חיפוש טווחי
# bool	{"bool": {"must": [...], "should": [...], "must_not": [...]}}	שילוב תנאים