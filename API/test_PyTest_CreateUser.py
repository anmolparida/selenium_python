import requests
import json
import jsonpath

api_url = "https://reqres.in/api/users"

def test_create_new_user():

    print('PyTest')
    response = requests.get(api_url)
    print(response)
    print(response.status_code)
    assert response.ok
    assert response.status_code == 200
    json_response = json.loads(response.text)

    # PARSING THE VALUES
    data = jsonpath.jsonpath(json_response, 'data')
    print(data)
    print('len of data:', len(data))

    for val in json_response['data']:
        print(val['first_name'], val['last_name'])