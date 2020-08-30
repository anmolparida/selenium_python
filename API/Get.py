import requests
import json
import jsonpath


"""
**************************************************
Print all first_name and last_name inside data
**************************************************
"""
print('*'* 50)
print('Print all first_name and last_name inside data')
print('*'* 50)

api_url = "https://reqres.in/api/users?page=2"

response = requests.get(api_url)
print(response)
print(response.status_code)
assert response.ok

json_response = json.loads(response.text)

# PARSING THE VALUES
data = jsonpath.jsonpath(json_response, 'data')
print(data)
print('len of data:', len(data))

for val in json_response['data']:
    print(val['first_name'], val['last_name'])