from translate import Translator

#create the translator object variable something idk what python is
translator = Translator(to_lang='bn', from_lang='en')

#r is read only
#w is for rewrite 
#w+ is for read and write
#a is for append
#for inputting the foreign langauge code
file1 = open('input.txt', 'r', encoding='utf-8')

raw_text = file1.read()

#create the translator
output = translator.translate(raw_text)

#for ouputting the translated version
#don't know whether i'm just going to write over the file given or create a new one but we'll see
file2 = open('output.txt', 'w', encoding='utf-8')
file2.writelines(output)


file1.close
file2.close