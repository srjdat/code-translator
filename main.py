import requests

#open the file that has the input text in another language
file1 = open('input.txt', 'r', encoding='utf-8')
#open the file where i output it into
file2 = open('output.txt', 'w', encoding="utf-8")
#read the file in
file_input = file1.read()



#########
#this is for the translation part
#########



#this api is for getting the translations -- ends up with some errors which we later on fix
url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

#automatically detects what language the code is in and translates into english 
#text being the variable we set earlier
payload = {
	"from": "auto",
	"to": "en",
	"text": file_input
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "d803947fb9msh2836690cd477237p144b80jsn6b14d20d2c4d",
	"X-RapidAPI-Host": "google-translate113.p.rapidapi.com"
}

#gets the response and stores it in the response variable
response = requests.post(url, data=payload, headers=headers)

#i then make this variable for an array type thing idek what it is i think dict idk anyways i store it in there
translation_data = response.json()
#get the translation into a variable
translation = translation_data['trans']



#########
#since you cannot 100% accurate translate everything i decided to use ai in order to fix the loose ends
#ai fixing portion
########



url = "https://open-ai21.p.rapidapi.com/chatgpt"

#payload things, general stuff nothing too crazy just the api call
payload = {
	"messages": [
		{
			"role": "user",
			"content": f"{translation} \ncan you just give me the fixed code and nothing else"
		}
	],
	"web_access": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "d803947fb9msh2836690cd477237p144b80jsn6b14d20d2c4d",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}

#same thing as before
response = requests.post(url, json=payload, headers=headers)

ai_fixing = response.json()
final_result = ai_fixing['result']

#first part is to remove the 
file2.write(final_result.replace("```python", "").replace("```", "").strip())

#close the files
file1.close
file2.close