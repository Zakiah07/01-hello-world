#using while loops to build a guessing game
secret_number = 9 #while loops can have else part
guess_count = 0
guess_limit = 3
while guess_count < guess_limit: 
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break #to terminate our loop
else:
    print('Sorry, you failed')

