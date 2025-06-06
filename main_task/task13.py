#Write a program that takes the email and password as input from a user and 
# checks if they are equal to “admin@mail.com” and 
# password is “Admin@123” ,
#  if so then print  “Login is Successful” and 
# if not print “Invalid username or password”. 
# ONLY accept 3 tries after which it notifies you that you have been blocked.
email="admin@mail.com"
password="Admin@123"
attempts=3
for s in range(1,attempts+1):
    email_input=input("Enter email: ")
    password_input=input("Enter password: ")
    remaining=attempts-s
    if email_input==email:
        if password_input==password:
            print("Login is Successful")
            break
        else:
            print("Invalid password")
            print(f"{remaining} attempts left")
    else:
        if remaining>0:
            print(f"{remaining} attempts left")
            print("Invalid email")
        else:
            print("You have been blocked")

