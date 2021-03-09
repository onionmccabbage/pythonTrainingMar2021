# we can access end-points using a URL and the 'requests' package
# NB we will need to install the requests package
import requests
import json

# we can very easily access any punlic api end-point like this. xml, json, text, html, bytes ANYTHING
result = requests.get('https://jsonplaceholder.typicode.com/photos/42')
print(type(result.json())) # convert the retrieved json to a Python dict
# we can dump the dict into a string using json.dumps()
result_str = json.dumps( result.json() )
print(type(result_str))

# NB we could just retrieve result.text() and avoid the dict!!!