# Write a program which gets a phone number from a form input or terminal.
# Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. 
# Convert the number to start with +254… 
phone_number=input("enter phone number: ")
phone_number=phone_number.strip()
phone_number={f"+254{phone_number[-9:]}"}
print(phone_number)

#teacher's work
if phone_number.startswith('+254') and len(phone_number)==13:
    valid=phone_number