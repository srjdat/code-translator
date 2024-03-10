import requests


#open a file for outputting
file1 = open('input.txt', 'r', encoding='utf-8')

file_input = file1.read()

#print(file_input)

url = "https://google-translate113.p.rapidapi.com/api/v1/translator/text"

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

response = requests.post(url, data=payload, headers=headers)

data = response.json()

translation = data['trans']
test = "stringnamechickenbutt"

file2 = open('output.txt', 'w')
file2.write(translation.replace('otherwise', 'elif').replace('Prints', 'print'))

file1.close
file2.close


#only other option i can think of to fix this translation issue is to use an AI api and call it and make it fix the code and put it into the file 
#that's enough coding for today i am now gonna go to sleep i have had enough i can't take this anymore someone please help me