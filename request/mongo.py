import requests

url = "http://127.0.0.1:8001/mongo/"
data = {"name": "David", "age": 36}

response = requests.post(url, json=data)
print(response.json())

# curl -X POST "http://127.0.0.1:8001/mongo/" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "David", "age": 36}'
url = "http://127.0.0.1:8001/mongo/"

response = requests.get(url)
print(response.json())

# curl -X GET "http://127.0.0.1:8001/mongo/"

id = "123"  # id של המסמך
url = f"http://127.0.0.1:8001/mongo/{id}"
data = {"age": 37}

response = requests.put(url, json=data)
print(response.json())

# curl -X PUT "http://127.0.0.1:8001/mongo/123" \
#      -H "Content-Type: application/json" \
#      -d '{"age": 37}'

id = "123"
url = f"http://127.0.0.1:8001/mongo/{id}"

response = requests.delete(url)
print(response.json())

# curl -X DELETE "http://127.0.0.1:8001/mongo/123"


