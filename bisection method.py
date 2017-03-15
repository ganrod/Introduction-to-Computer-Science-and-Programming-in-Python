high = 100
low = 0
pcGuess = False

print('Imagine a number between 0 and 100.')

while pcGuess == False:
    guess = (high + low)/2
    print('Is your guess #' + str(guess) + '?')
    user_inp = raw_input("Enter 'h' if the guess is too high. Enter 'l' if the guess is too low. Enter 'c' if I guessed correctly. ")

    if user_inp == 'c':
        print('We got it!')
    elif user_inp == 'l':
        low = guess
    elif user_inp == 'h':
        high = guess
    else:
        print("Didn't understand your input.")

print('Your number is: ' + str(guess))