#Write a program that prints the largest of 4 inputs taken as input from a user.
w=input("enter input: ")
x=input("enter input: ")
y=input("enter input: ")
z=input("enter input: ")
if len(w)>len(x) and len(w)>len(y) and len(w)>len(z):
    print(w)
elif len(x)>len(w) and len(x)>len(y) and len(x)>len(z):
    print(x)
elif len(y)>len(x) and len(y)>len(w) and len(y)>len(z):
    print(y)
else:
    print(z)