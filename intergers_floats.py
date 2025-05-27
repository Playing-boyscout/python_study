x=99
y=5
#modulus
q=x%y
print(q)

#floor //
a=x//y
print(a)

text="enter integer: "
int1=input('enter first number: ')
int2=input('enter second number: ')
sum=int1+int2
print(sum)

#rounding off
temp=56.8926
temp=round(temp,3)
print(temp)

#converting a float
temp=56.8926
temp=str(temp)
temp=temp[3:]
print(temp)
temp=f"{temp[0]}.{temp[1:]}"
temp=float(temp)
print(temp)

#diff approach
temp=56.8926

#temp111.0789 to 78.9
temp = 111.0789
temp = str(temp)
temp = temp[5:]
temp =f"{temp[0:2]}.{temp[2:]}"
temp = float(temp)
print(temp)

#concutination method
temp = 111.0789
temp = str(temp)
temp = temp[5:]
temp=temp[0:2]+'.'+temp[2]
temp=float(temp)
print(temp)
