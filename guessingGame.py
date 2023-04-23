secret_number = 9
guesses_made = 0
guesses_limit = 5
while guesses_made < guesses_limit:
    guess = int(input('Guess: '))
    guesses_made += 1
    if guess == secret_number:
        print('you won')
    elif guess != secret_number:
        print('incorrect guess, try again')
        
else:
    print('you have failed the game')  
    
     