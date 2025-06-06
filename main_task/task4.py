#Write a program which accepts email as form input or from terminal.
#  Validate the email by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email=input("enter email: ")
email=email.lower().strip()
valid_email=email
if valid_email.count("@")==1:
    if valid_email.count(".")==0:
        print("Invalid email")
    else:
        print(f"{valid_email} is a valid email")
else:
    print("Invalid email")
