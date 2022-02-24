invalidGuesses = 6  # 6 invalid guesses
guessed = ""  # contains correctly guessed letters


def success():  # user has successfully guessed the word
    print("\t\t---- CONGRATULATIONS!")


def fail():  # user has failed to guess the word
    print("\n---- Sorry, you lose!")


def display():
    count = 0  # no. of letters guessed correctly
    for c in word:  # for every letter in the word
        if c in guessed:  # if letter match guessed
            print(c, end=" ")  # thus, print letter/s
            count += 1  # then, increase count
            if len(c) >= 2:  # if letters have duplicate
                count += len(c)  # thus, increase count
            if count == len(word):  # check if the no. of correctly guessed letters is equal to the length of the word
                success()  # thus, the user has guessed the word
                exit()  # exit the program after user has successfully guessed the word
        else:  # if letter is not in the guessed
            print("_", end=" ")  # thus, print underscore to hide


def attempts():
    print("\nremaining invalid guesses: " + str(invalidGuesses))  # display the remaining invalid guesses


word = input("Enter a secret word: ")  # the user will input a word first
print("You have a " + str(len(word)) + " letter word to guess.")  # display the total number of characters
display()  # display the word as hidden through underscore/s
attempts()
# start guessing all the letters
while invalidGuesses > 0:  # the user can only continue playing if the invalid guesses are greater than 0

    guess = input("\nGuess any letter: ")  # the user will input a letter

    if guess in word:  # if the letter is in the word
        guessed += guess  # then, add the new guess to the guessed
        display()  # display guessed
        print("\n")
    else:
        invalidGuesses -= 1  # else, decrement the invalid guesses by 1
        display()  # display guessed
        attempts()

    if invalidGuesses == 0:  # if invalid guesses reaches 0
        fail()  # thus, user has failed to guess the word
