text=" JOHn ."
text_change=text.strip().lower().replace(".","")
print(text_change)

#slicing
sentence_one="The Dog Breed is German Shepherd"
sentence_one_sliced=sentence_one[8:23]
print(sentence_one_sliced)
sentence_two="Defeats for the Clinton forces, this was her moment of triumph"
sentence_two_sliced=sentence_two[-46:-32]
print(sentence_two_sliced)

#splitting
sentence=  "The lazy dog; ran so fast; it hit the wall."
sentence_split=sentence.split(";")
print(len(sentence_split))

first_name=" Joh.n"
last_name=" Do,e"
first_change=first_name.strip().replace(".","")
last_change=last_name.strip().replace(",","")
full_name=first_change + " " +last_change
print(full_name)

r='["E","W","C"]'
r_change=r.replace('"','').replace(',','').replace('[','').replace(']','')
print(r_change)

sentence1=input('enter a sentence : ')
sentence=sentence1.split(' ')
print(sentence)
print(len(sentence))


sentence_title=sentence.title()
print(sentence_title)

sentence_reverse=sentence[::-1]
print(sentence_reverse)


text ="BAD habits are hard to break!  "
text = text.replace('BAD','good')
text =text.strip()
print(text)

#clean email and extract domain
email= "   John.Doe@GMAIL.COM  "
email=email.strip()

email=email.lower()
print(email.find())

#formatted strings

