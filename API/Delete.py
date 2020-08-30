import requests
import json
import jsonpath


api_url = "https://reqres.in/api/users/2"

respose = requests.delete(api_url)

print(respose.status_code)
print(respose)

assert respose.status_code == 204