import requests
import json
import jsonpath


api_url = "https://reqres.in/api/users?page=2"

response = requests.get(api_url)

# response in the form of string
print(response.text)

# validate response code
assert response.status_code == 200
assert response.ok
# assert response.status_code == 202 # AssertionError

"""
Parse response into JSON format
"""
# response in the form of string
json_response = json.loads(response.text)
print(json_response)

# Apply jsonpath
print('\nApply jsonpath')
x = jsonpath.jsonpath(json_response, 'total')
print(x[0])

y = jsonpath.jsonpath(json_response, "data[0].first_name")
print(y)







