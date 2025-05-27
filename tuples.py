grades=('A','B','C','D','Credit','Pass','Fail')
print(grades[-2])
print(type(grades))

#covert to a list
grades=list(grades)
print(type(grades))
grades[-1]='E'
print(grades)
grades=tuple(grades)
print(grades)

#exercise
days=("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days[-5])
print(len(days))
days=list(days)
days[-4]='thur'
days=tuple(days)
print(days)
print(type(days))