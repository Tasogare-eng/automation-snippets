import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users[0]["name"])

# Leanne Graham