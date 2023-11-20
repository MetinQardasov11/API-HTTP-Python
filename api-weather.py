import requests

url = 'http://api.weatherapi.com/v1/current.json'
api_key = '3e3b7d1de35046b0ab6124437231911'

city = input('City: ')

guess = requests.get(url,params={
    'key' : api_key,
    'q' : city,
    'lang' : 'eng'
})

information_baku = guess.json()
country = information_baku['location']['country']
city = information_baku['location']['name']
degree_baku = information_baku['current']['temp_c']
text_weather = information_baku['current']['condition']['text']
print(f'It is currently {degree_baku} degrees and {text_weather} in {city} where is located {country}.')