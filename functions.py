def triangle_area(height,base):
    area=height*base*0.5
    print(area)
triangle_area()

def check_number():
    num=30
    if num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

#function to calculate area of a rectangle
#create a function that displays the largest number among 3 numbers
def rectangle_area(length,width):
    area=length*width
    print(area)
rectangle_area(14,7)

def largest_number(number1,number2,number3):
    if number1>number2 and number1>number2:
        print(number1)
    elif number2>number1 and number2>number3:
        print(number2)
    else:
        print(number3)
num1=input("enter firt number:")
num2=input("enter second number:")
num3=input("enter third number:")
largest_number(num1,num2,num3)
