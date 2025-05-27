user_credit_score=input("enter your credit score: ")
user_credit_score=int(user_credit_score)
if user_credit_score>700:
    annual_income=input("enter your annual income: ")
    annual_income=int(annual_income)
    if annual_income>50000:
        print("Loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit score too low")