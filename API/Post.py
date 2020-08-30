import requests
import json
import jsonpath


api_url = "https://reqres.in/api/users/"


with open("Post_Data.json", mode='r', encoding='utf-8') as f :
    json_input = f.read()
# print(json_input)

request_json = json.loads(json_input)
# print(request_json)

response = requests.post(api_url,request_json)
print(response)
print(response.content)
assert response.status_code == 201

json_response = json.loads(response.text)
print(json_response)
print(json_response['id'])

print(response.headers['Content-Length'])
print(response.headers.get('Content-Length'))

