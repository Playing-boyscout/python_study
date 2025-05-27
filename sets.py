from tkinter import Y


numbers={11,12,13,14,15,16,17}
print(type(numbers))
print(numbers)

x=["kevin","alex","Pauline","Brian","Kevin","alex"]
print(x)
x=set(x)
x=list(x)
print(x)


days ={"monday","tuesday","wednesday","thursday","friday","saturday","sunday","sunday","sunday","sunday",}
print(days)
days.remove("friday")
days.remove("sunday")
print(days)

days.add("friday")
days.add("sunday")
print(days)

#difference
x={1,2,3,4,5,6,7}
y={5,6,7,8,9,10}
z=x - y 
print(z)

z=y.difference(x)
print(z)

#union
z=x.union(y)
print(z)

#symmetric_difference
z=x.symmetric_difference(y)
print(z)

#intersection
z=x.intersection(y)
print(z)

