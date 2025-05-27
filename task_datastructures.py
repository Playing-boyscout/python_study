my_ds=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]

#print  KES
print(my_ds[3][2]["currency"])
#print 560
print(my_ds[2])
#print Maths
print(my_ds[3][1])
#Adding another key amount=90 on the dictionary
my_ds[3][2]['amount']='90'
print(my_ds)
#reverse 987 to 789
print(my_ds[4])
print(type(my_ds[4]))
str_change=str(my_ds[4])
print(type(str_change))
print(str_change[::-1])
#change name john to jane
my_ds[5]=list(my_ds[5])
print(my_ds)
my_ds[5][1]="Jane"
print(my_ds)
my_ds[5]=tuple(my_ds[5])
print(my_ds)  

x=(560)
print(type(x))