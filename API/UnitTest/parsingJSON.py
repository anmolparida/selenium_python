# We will be using this url for the current program
# 'https://www.upcitemdb.com/api/explorer#!/lookup/get_trial_lookup'

# https://api.upcitemdb.com/prod/trial/lookup?upc=885909950805 (Key: upc, Value: 885909950805)

import requests
import json

baseURL = 'https://api.upcitemdb.com/prod/trial/lookup?'

parameters = {'upc': '885909950805'}  # barCode input

response = requests.get(baseURL, params=parameters)

# print(response.url)

content = response.content
info = json.loads(content)

# print(type(info)) >> dict
# print(info)


item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']

print(title)
print(brand)
