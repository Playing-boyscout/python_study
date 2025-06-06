number=input("enter number: ")
number=int(number)
if number%2==0:
    if number%4==0:
        print("divisible by 4 and an even number")
    else:
        print("even number")
else:
    print("odd number")