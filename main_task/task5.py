input1=input("enter input: ")
input2=input("enter input: ")
input3=input("enter input: ")
if len(input1)>len(input2) and len(input1)>len(input3):
    print(f"{input1} is the largest of the three")
elif len(input2)>len(input1) and len(input2)>len(input3):
    print(f"{input2} is the largest of the three")
else:
    print(f"{input3} is the largest of the three")