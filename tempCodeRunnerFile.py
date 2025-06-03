# Write a program that displays a numbers 1 to 50 inside a list.
inside_list=[]
for en in range(1,51):
    inside_list.append(en)
print(inside_list)

# From 1 above display the ones divisible by 7 or 5 inside a list.
divisible_range=[]
for e in range(1,51):
    if e%5==0 or e%7==0:
        divisible_range.append(e)
print(divisible_range)

#Find sum and average of values in the range between 10 to 40.
numbers=range(10,40)
sum=0
for a in numbers:
    sum=sum+a
print(sum)
average=sum/len(numbers)
print(average)

#Put in a list the first 10 odd numbers between 10 to 50. 
odd_num=[]
for s in range(10,50):
    if s%2!=0:
        odd_num.append(s)
        if len(odd_num)==10:
            print(odd_num)

#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=input("enter number: ")
number=int(number)
for i in range (0, 11):
    mult=i*number
    print(f'{number}*{i}={mult}')

#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
num=range(1,50)
count=0
for t in num:
    if t%2==0:
        count=count+1
        print(t)
print(count)

# s1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
ls1=[("jay",'20'),("Mo",'30'),("Mya",'32')]
ls1[0],[1],[2]=list
print(ls1)
