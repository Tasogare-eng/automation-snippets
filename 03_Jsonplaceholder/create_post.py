import requests

payload = {
    "title": "Test Post",
    "body": "This is a test post.",
    "userId": 1
}
response = requests.post("https://jsonplaceholder.typicode.com//posts", json=payload)
print(response.json())

# {'title': 'Test Post', 'body': 'This is a test post.', 'userId': 1, 'id': 101}