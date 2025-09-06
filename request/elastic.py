url = "http://127.0.0.1:8002/elastic/"
data = {"name": "David", "age": 36}

response = requests.post(url, json=data)
print(response.json())
#
# curl -X POST "http://127.0.0.1:8002/elastic/" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "David", "age": 36}'

url = "http://127.0.0.1:8002/elastic/"
query = {"name": "David"}

response = requests.get(url, json=query)
print(response.json())

# curl -X GET "http://127.0.0.1:8002/elastic/" \
#      -H "Content-Type: application/json" \
#      -d '{"name": "David"}'

id = "1"
url = f"http://127.0.0.1:8002/elastic/{id}"
data = {"age": 37}

response = requests.put(url, json=data)
print(response.json())

# curl -X PUT "http://127.0.0.1:8002/elastic/1" \
#      -H "Content-Type: application/json" \
#      -d '{"age": 37}'

id = "1"
url = f"http://127.0.0.1:8002/elastic/{id}"

response = requests.delete(url)
print(response.json())

# curl -X DELETE "http://127.0.0.1:8002/elastic/1"

