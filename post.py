import requests

response = requests.post('https://jsonplaceholder.typicode.com/posts',data={
    "title" : "attempt",
    "body" : "attempt",
    "userId" : 1
    }
)

result = response

print(result.text)
print(result.json())