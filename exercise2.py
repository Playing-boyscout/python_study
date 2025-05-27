text=input('enter a sentence: ')
text1=text.split(' ')
print(len(text))

sentence1=text.title()
print(sentence1)

sentence2=text[::-1]
print(sentence2)

#conversion of text
sentence="good habits are hard to break!"
sentence_change=sentence.replace('good','BAD').strip()
print(sentence_change)

#clean email and extract domain
email= "    John.doe@gmail.com  "
email_clean=email.strip().lower()
print(email_clean)

#clean names and create a formatted sentence
first="john"
last="DOE"
hobby="  Reading Books  "
first_change=first.capitalize()
last_change=last.capitalize()
hobby_change=hobby.strip()
sentence_formatted=f"My name is {first_change} {last_change} and I love {hobby_change}"
print(sentence_formatted)