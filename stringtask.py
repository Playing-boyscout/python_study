name ="JOHn ."
name_result =name.strip().lower().replace(".","")
print(name_result)

sentence_one ="The Dog Breed is German Shepherd"
sentence1_sliced =sentence_one[8:23]
print(sentence1_sliced)
sentence_two ="Defeats for the Clinton forces, this was her moment of triumph"
sentence2_sliced = sentence_two[16:30]
print(sentence2_sliced)

sentence="The lazy dog; ran so fast; it hit the wall."
sentence_split= sentence.split(";")
print(len(sentence_split))

first_name = "  Joh.n"
last_name = "   Do,e"
clean_first = first_name.strip().replace(".", "")
clean_last = last_name.strip().replace(",", "")
full_name = clean_first + " " + clean_last
print(full_name) 