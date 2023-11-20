import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
result = response
type_response = type(response)
code = response.status_code
information = response.headers
Content_type = response.headers['Content-Type']
url = response.url
encode = response.encoding
data = response.text
data_type = type(response.text)
todo = json.loads(response.text)
todo_type = type(todo)


print(result)
print(type_response)
print(code)
print(information)
print(Content_type)
print(url)
print(encode)
print(data)
print(data_type)
print(todo)
print(todo_type)
print(todo[0]['title'])



for item in todo:
    print(item['title'])


for item in todo:
    if item['userId'] == 1:
        print(item['title'])
