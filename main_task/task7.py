students_marks=input("enter student's mark: ")
students_marks=int(students_marks)
if students_marks>=0 and students_marks<=100:
    if students_marks>=79:
        print("A")
    elif students_marks>=60:
        print("B")
    elif students_marks>=49:
        print("C")
    elif students_marks>=40:
        print("D")
    else:
        print("E")
else:
    print("student marks must be between 0 and 100")
