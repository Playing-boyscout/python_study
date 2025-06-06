# Write a program that takes input of 2 values and adds them.
#  The program should only accept numbers and floats only or 
# otherwise display an error “invalid character entered” and 
# take the user to re-enter the inputs .
while True:
    try:
        input1=(input("enter the first number: "))
        input1=int(input1) or float(input1)
        input2=(input("enter the second number: "))
        input2=int(input2) or float(input2)
        sum=input1+input2
        print("sum of the numbers is:",sum)
        break
    except:
        print("invalid character entered try again")