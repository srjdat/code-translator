from uu import encode
import requests
import json

#method for displaying
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=1)
    print(text)

#the url for api
url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

#what we want to translate
#from what lang to what lang
payload = {
	"q": "Hello, world!",
	"target": "bn",
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

##open a file for outputting
file1 = open('json_output.txt', 'w')
#file1.write(response.json())
#print(response.json())


#get only the translated things
translated_text = response.json()['translations']
jprint(translated_text)