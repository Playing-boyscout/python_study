# Write a program that displays a numbers 1 to 50 inside a list.
# From 1 above display the ones divisible by 7 or 5 inside a list.
# Find sum and average of values in the range between 10 to 40.
# Put in a list the first 10 odd numbers between 10 to 50. 
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.
# inside_list=[]
# for en in range(1,51):
#     if en%5==0 or en%7==0:
#         inside_list.append(en)
# print(inside_list)

# numbers=range(10,40)
# sum=0
# for x in numbers:
#     sum=sum+x
# print(sum)
# average=sum/len(numbers)
# print(average)

# odd_numbers=[]
# for odd in range(10,50):
#     if odd%2==1:
#         odd_numbers.append(odd)
# print(odd_numbers[:10])

num=input("enter number: ")
num=int(num)
ener=range(1,10)
for a in ener:
    multiply=num*a
print(f'{num}*{a}={multiply}')

# even_numbers=range(1,50)

# for s in even_numbers:
    # if s%2==0:
    #     print(s)
        
# 

        
