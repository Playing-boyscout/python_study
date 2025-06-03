number='1650'
attempts=3
for i in range(1,attempts+1):
    guess=input('Guess the number: ')
    if guess==number:
        print("You guessed right")
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'You have {remaining_attempts} attempts left')
        else:
            print('you have run out of attempts')