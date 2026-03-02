print(f"{50*"="}")
print(f"Task 1 — Building a JSON Structure")
print(f"{50*"="}")

import json

user = {
    "name": "Jnaneswar",
    "age": 30,
    "email": "jnaneswar@gmail.com",
    "is_active": True,
    "skills": ["Artificial Intelligence", "Machine Learing", "Data Science"]
}

json_string = json.dumps(user)
print(json_string)


print(f"{50*"="}")
print(f"Task 2 — Parse an API Response")
print(f"{50*"="}")

import json

api_response = '''{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'''

data = json.loads(api_response)

user_name = data["data"]["username"]
user_score = data["data"]["score"]
print(user_name)
print(user_score)
print(f'''A message: "User {user_name} scored {user_score} points"''')


print(f"{50*"="}")
print(f"Task 3 — Handle Nested JSON")
print(f"{50*"="}")

import json

user = {
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}

user_city = user["address"]["city"]
user_zipcode = user["address"]["zip"]
print(user_city)
print(user_zipcode)

user["address"]["country"] = "India"

print(user)
