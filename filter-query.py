# url?key1=value1&key2=value2

import requests

# Filter: userId = 1, completed = True
response_1 = requests.get('https://jsonplaceholder.typicode.com/todos?userId=1&completed=true')

# OR

response_2 = requests.get('https://jsonplaceholder.typicode.com/todos',params={
    "userId" : 2,
    "completed" : 'false'
})

list_1 = response_1.json() 
list_2 = response_2.json() 


# print(response_1.text)
# print(list_1[0]['title'])
# print(response_2.text)
print(list_2[0]['title'])

