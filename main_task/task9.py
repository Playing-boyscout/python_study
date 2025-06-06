#Write a program called stars. 
# It should prompt the user for a number, and it should print the number of stars till the number entered.
stars=input("enter a number: ")
stars=int(stars)
for i in range(1,stars+1):
    print(i*'*')