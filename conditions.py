a=20
b=50

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

x=50
marks=input("enter marks: ")
marks=int(marks)
if marks>x:
    print("pass")
else:
    print("fail")

password="Chebwogrn345"
password_input=input("enter password: ")
if password_input==password:
    print("Access Granted")
else:
    print("Access Denied")


#grading system
marks=input("enter marks: ")
marks=int(marks)
if marks>80:
    print('A')
elif marks>70 and marks<=80:
    print('B')
elif marks>60 and marks<=70:
    print('C')
elif marks>50 and marks<=60:
    print('D')
else:
    print('Fail')

#nested if statements
age=input("what is your age: ")
age=int(age)
if age >=18:
    print("you are allowed to enter")
    if age>=21:
        print("you are allowed to drink")
    else:
        print("you are not allowed to drink")
else:
    print("You are not allowed to enter")