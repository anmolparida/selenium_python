# Video : https://www.youtube.com/watch?v=TJ5xTo4xiGY&list=PLIMhDiITmNrILoYaVsrxwteH6LqMr07uX&index=2

'''

GET	    Retrieve representation of the member resource in the response body.
POST	Create a member resource in the collection resource using the instructions in the request body. The URI of the created member resource is automatically assigned and returned in the response Location header field.
PUT	    Replace all the representations of the member resources of the collection resource with the representation in the request body, or create the collection resource if it does not exist.
PATCH	Update all the representations of the member resources of the collection resource using the instructions in the request body, or may create the collection resource if it does not exist.
DELETE	Delete all the representations of the member resources of the collection resource.	Delete all the representations of the member resource.


Response Status Code	        Meaning

200     Ok                      Successful requests other than creations and deletions.
201     Created                 Successful creation of a queue, topic, temporary queue, temporary topic, session, producer, consumer, listener, queue browser, or message.
204     No Content              Successful deletion of a queue, topic, session, producer, or listener.

400     Bad Request             The path info doesn't have the right format, or a parameter or request body value doesn't have the right format, or a required parameter is missing, or values have the right format but are invalid in some way (for example, destination parameter does not exist, content is too big, or client ID is in use).
403     Forbidden               The invoker is not authorized to invoke the operation.
404     Not Found               The object referenced by the path does not exist.
405     Method Not Allowed      The method is not one of those allowed for the path.
409     Conflict                An attempt was made to create an object that already exists.

500     Internal Server Error   The execution of the service failed in some way.
503     xService Unavailable

'''
import requests
import json
import jsonpath_rw
import  jsonpath_rw_ext


baseURL = "https://reqres.in//api/users?page=2"

response = requests.get(baseURL)

print('\n', response)
print('\n', response.content)
print('\n', response.headers)

# parse response to json format

json_response = json.loads(response.text)
print(json_response)