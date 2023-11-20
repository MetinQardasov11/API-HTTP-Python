import requests
import json

api_key = '821ed22090582f60c0b5518d'
url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/'

convert_currency = input('Convert to currency: ') # For example, USD
get_currency = input('Get currency: ') # For example, AZE
quantity = int(input(f'How much {convert_currency} do you want to convert?: '))

result = requests.get(url + convert_currency)
result_json = json.loads(result.text)

print('1 {0} = {1} {2}'.format(convert_currency,result_json['conversion_rates'][get_currency],get_currency))
print('{0} {1} = {2} {3}'.format(quantity,convert_currency,
                                round(result_json['conversion_rates'][get_currency]*quantity,2),get_currency))