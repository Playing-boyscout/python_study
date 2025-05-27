student = {
    'name': 'JJ',
    'age': 19,
    'email':'jeweljelagat@gmail.com',
    }
print(type(student))
print(student)

#accessing values in a dictionary
print(student['email'])

#modify data in dict
student['age']=20

#add
student['phone no']='0797494923'
print(student)
student['occupation']='Ambassador'
print(student)

student['location']={'town':'nakuru','address':'1540','street':'Kimathi'}
print(student)
print(student['location']['street'])

student['skills']=['coding','team player','skating','leadership skills']
print(student['skills'][1])

