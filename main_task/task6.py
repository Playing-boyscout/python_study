#Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”.
#If the password is correct access is granted.
# After you show them a message , the account is blocked.
password="admin@123"
attempts=4
for t in range(1,attempts+1):
    password_input=input("enter password: ")
    if password_input==password:
        print("Access Granted")
        break
    else:
        remaining_attempts=attempts-t
        if remaining_attempts>0:
            print(f"{remaining_attempts} reamining attempts left")
        else:
            print(f"Account blocked")