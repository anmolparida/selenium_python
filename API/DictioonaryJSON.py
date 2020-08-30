"""
parsing JSON using a dictionary
"""
import json
# TypeError: the JSON object must be str, bytes or bytearray, not dict
d = '{"k1": "val1", "k2": "val2"}'

jsonResult = json.loads(d)
print(jsonResult)
