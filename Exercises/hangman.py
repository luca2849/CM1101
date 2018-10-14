word = "HANGMAN"
won = False
guessed_letters = []
arr_word = list(word)
while won == False:
    guess = input("Guess a letter > ")
    if guess.upper() in guessed_letters:
        print("Already Guessed!")
    elif guess.upper() in word:
        guessed_letters.append(guess)
        print("Correct")
    else:
        print("Incorrect, guess again")
    if len(guessed_letters) == len(arr_word):
        won == True
        break
if won == True:
    print("=======================")
    print("Congratulations!")
    print("You have won the game!")
    print("=======================")
