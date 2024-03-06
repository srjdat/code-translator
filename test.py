from ast import parse
from uu import encode
import requests
import json

#open a file for outputting
file1 = open('json_output.txt', 'w+')

#method for displaying
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    file1.writelines(text)

#the url for api
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

#what we want to translate
#from what lang to what lang
payload = {
	"q": "Hello, how are you doing?",
	"target": "zh",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "d803947fb9msh2836690cd477237p144b80jsn6b14d20d2c4d",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

#get the response
response = requests.post(url, data=payload, headers=headers)


data = str(response.json())
parsed_json = json.load(data)
print(parsed_json)


file1.close
