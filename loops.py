fruits=['Apple','Banana','Oranges','Melon']
for i in fruits:
    print(i)

numbers=list(range(100,201))
for num in numbers:
    if num%2!=0:
        print(num)
#store even numbers from 200 to 500 in a list
even_numbers=[]
for en in range(200,501):
    if en%2==0 :
        even_numbers.append(en)
print(even_numbers)