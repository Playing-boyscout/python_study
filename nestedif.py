# user_credit_score=input("enter your credit score: ")
# user_credit_score=int(user_credit_score)
# if user_credit_score>700:
#     annual_income=input("enter your annual income: ")
#     annual_income=int(annual_income)
#     if annual_income>50000:
#         print("Loan approved")
#     else:
#         print("Income requirement not met")
#else:
    # print("Credit score too low")
#Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. 
# If both conditions are true, print "Excellent student",
#  otherwise print "Good score, but attendance needs improvement"
# student_score=input("enter student's score: ")
# student_score=int(student_score)
# attendance=input("student's attendance score: ")
# attendance=int(attendance)
# if student_score>90:
#     if attendance>80:
#         print("Excellent student")
#     else:
#         print("Good score but attendance needs improvement")
# else:
#     print("Score needs improvement")

#Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#If the account type is "Standard":
#Check if the amount is above 500:
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."

# account_type=input("what type of account is the user using:(Standard/Premium)")
# transaction_amount=input("what is your transaction amount: ")
# transaction_amount=int(transaction_amount)
# if account_type=="Standard":
#     if transaction_amount>500:
#         print("Transaction exceeds the limit for Standard accounts.")
#     else:
#         print("Transaction approved.")
# elif account_type=="Premium":
#     if transaction_amount>1000:
#         print("Transaction exceeds the limit for Premium accounts.")
#     else:
#         print("Transaction approved")
# else:
#     print("Wrong account type")

#Assume start_date = '2024-01-01' and end_date = '2024-12-31'.
#Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".
# start_date='2024-01-01'
# end_date='2024-12-31'
# if end_date>start_date:
#     print("Valid period")
# elif start_date>end_date:
#     print("Invalid period")
# else:
#     print("One-day period")

# # #Given two strings str1 and str2, 
# # #write a conditional statement that checks:
# # #If str1 is longer than str2, print "str1 is longer".
# # #If str2 is longer than str1, print "str2 is longer".
# # #If both have equal length, print "Both are of equal length".
# str1=input("enter text: ")
# str2=input("enter text: ")
# if len(str1)>len(str2):
#     print("str1 is longer")
# elif len(str2)>len(str1):
#     print("str2 is longer")
# else:
#     print("Both are of equal length")

# #.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105,
# #write a conditional statement that:
# #Prints "Access Granted" if user_id is in valid_ids.
# #Prints "Access Denied" if user_id is not in valid_ids.
# valid_ids=[101,102,103]
# user_id=input("enter user id: ")
# user_id=int(user_id)
# if user_id in valid_ids:
#     print("Access Granted")
# else:
#     print("Access Denied")

# #Given a variable value that could be of any type, 
# #write a conditional statement that:
# #Prints "String Detected" if value is a string.
# #Prints "Integer Detected" if value is an integer.
# #Prints "Unknown Type" for any other type.
# X=34
# if type(X)==str:
#     print("String Detected")
# elif type(X)==int:
#     print("Integer Detected")
# else:
#     print("Unknown Type")

# Given x = 7 and y = 14, 
# write nested conditional statements that print:
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.
x=72
y=1
if y%2==0:
    if x%2==0:
        print("x and y are both even")
    else:
        print("Only y is even")
else:
    if x%2!=0:
        print("Neither x nor y are even")
    else:
        print("Only x is even")