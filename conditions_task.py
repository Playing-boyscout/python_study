A=input("enter number: ")
A=int(A)
B=input("enter number: ")
B=int(B)
C=input("enter number: ")
C=int(C)
if A>B and A>C:
    print(f"{A} is the largest number")
elif B>A and B>C:
    print(f"{B} is the largest number")
else:
    print(f"{C} is the largest number")

#4 inputs printing the larsgest no.
w=input("enter number: ")
w=int(w)
x=input("enter number: ")
x=int(x)
y=input("enter number: ")
y=int(y)
z=input("enter number: ")
z=int(z)
if w>x and w>y and w>z:
    print(f"{w} is the largest number")
elif x>w and x>y and x>z:
    print(f"{x} is the largest number")
elif y>x and y>w and y>z:
    print(f"{y} is the largest number")
else: 
    print(f"{z} is the largest number")

#temp scale
temp=input("temperature: ")
temp=float(temp)
if temp>30:
    print("The Temperature is too high")
elif temp>15:
    print("Normal temperature")
else:
    print("Cold temperature")

#Checking a variable
X=input('enter number: ')
X=int(X)
Y=input('enter number')
Y=int(Y)
if X>10 and X<20 and Y>100:
    print("Conditions met")
else:
    print("Conditions not met")

#Password verificaion
P="secret123"
password=input("enter password: ")
if password==P:
    print("Acces Granted")
else:
    print("Access Denied")

#checking a variable student score to be greater than 90
student_score=input("student's score: ")
student_score=int(student_score)
attendance=input("student's attendance percentage: ")
attendance=int(attendance)
if student_score>90 and attendance>80:
    print("Excellent student")
else:
    print("Good score,but attendance needs improvement")