from translate import Translator

#create the translator object variable something idk what python is
translator = Translator(to_lang='en', from_lang='bn')

#r is read only
#w is for rewrite 
#w+ is for read and write
#a is for append
file1 = open('MyFile.dat', 'r', encoding='utf-8')

#close the file
raw_text = file1.read()

#create the translator
output = translator.translate(raw_text)

file2 = open('MyFile.txt', 'w')


file1.close
file2.close