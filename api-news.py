import requests

url = 'https://newsapi.org/v2/top-headlines?country=tr&apiKey=9afb3a9b3f9f405da8815c6360868ed2'

response_tr = requests.get(url)

tr_news = response_tr.json()
print(tr_news['articles'][0])

tr_news_2 = response_tr.json()['articles']

for i in tr_news_2:
    print('Source name:',i['source']['name'])
    print('Title:',i['title'])
    print('url:',i['url'])
    

# OR

headline_url = 'https://newsapi.org/v2/top-headlines?'
everything_url = 'https://newsapi.org/v2/everything'

api_key = '9afb3a9b3f9f405da8815c6360868ed2'

# response_us = requests.get(url=headline_url,params={
#     'apiKey' : api_key,
#     'country' : 'us'
# })

# us_news = response_us.json()['articles']

response_football = requests.get(url=everything_url,params={
    'apiKey' : api_key,
    'q' : 'football',
    'language' : 'tr',
    'sortBy' : 'publishedAt'
})

football_news = response_football.json()['articles']

for i in football_news:
    print('Source name:',i['source']['name'])
    print('Title:',i['title'])
    print('url:',i['url'])
