from random import randint
import os

def main():

    print("Welcome to Hangman!\nYou have 6 guesses!\nAfter 6 guesses, the game will end.")

    word_bank = ["learn", "speak", "something", "try", "enjoy", "because", "than", "before", "oneself", "understand",
                 "become", "always"]

    word_buffer = []
    # this keeps track of what the answer is

    blank_buffer = []
    # this is the list of blanks that changes with every guess

    word = randint(0, len(word_bank))
    # choosing a random word from the bank
    # the end point changes based on how many words there are

    word_buffer.extend(word_bank[word])
    # this puts the chosen word into the word buffer

    word_deux = []
    word_deux.extend(word_bank[word])
    # this is making a reference list to compare to to tell when to finish the game

    for x in word_buffer:
        blank_buffer.append("_ ")
    # this is populating the blank buffer with a number of blanks
    # equal to the letters in the chosen word


    for x in blank_buffer:
        print(x, end=" ")
    # this prints out the blanks on screen neatly (initial blanks)

    user_prompt = "\nWhat is your guess? \n> "
    # this will store the guesses and be used to feed data into the func

    miss_box = []

    # keeps track of letters guessed and missed

    def placing_letters():
        guess = input(user_prompt)
        os.system('cls')
        # clears the screen so it doesn't get cluttered

        if guess.isalpha() == True and len(guess) == 1:

            if guess in word_buffer:
                print("There's a %s!" % guess)

                while guess in word_buffer:
                    guess_index = word_buffer.index(guess)
                    # finding the index of the guess-letter in the blank buffer

                    blank_buffer[guess_index] = guess
                    # changing the blank at the guess's index to the guess

                    word_buffer[guess_index] = 0
                """This whole loop changes multiple letter entries in the manufactured list
                This solves the problem of retrieving indices of multiple entries in a list"""

                print(" ".join(blank_buffer))
                # printing the new blank buffer with the replaced guess/index

                print(miss_box)
                """if the guess is actually in the word, this will exchange
                a blank in for the letter"""

            elif guess in blank_buffer:
                print("You've already guessed %s!" % guess)
                print(" ".join(blank_buffer))
                # ~~without this, the blank buffer doesn't display~~

                print(miss_box)
                pass

            else:
                if guess not in miss_box:
                    miss_box.append(guess)
                # this keeps the miss box from having multiple entries of the same value

                print("There's no %s." % guess)
                print(" ".join(blank_buffer))
                # ~~without this, the blank buffer doesn't display~~

                print(miss_box)
                pass
                """if the guess is not in the word, this will display
                the user's progress and pass"""

        else:
            print("That's not a correct guess.")
            print(" ".join(blank_buffer))
            # ~~without this, the blank buffer doesn't display~~

            if len(miss_box) > 0:
                print(miss_box)
            # this catches the multi-letter entries


    while word_buffer != blank_buffer:
        if blank_buffer != word_deux:
            placing_letters()
            # this keeps the game going as long as there are letters left to be guessed

            if len(miss_box) == 6:
                print("You've lost the game! Try again next time!")
                print("The correct answer was %s" % word_bank[word].upper())
                break
            # loss scenario, ends the game at the specified guess limit

        elif blank_buffer == word_deux:
            os.system('cls')
            print("Congratulations! You win!")
            print(" ".join(blank_buffer))
            # ~~without this, the blank buffer doesn't display~~

            print(miss_box)
            break

        """This if loop is to finish the game when the value of the reference var (word_deux)
            equals the current blank buffer"""

    input()

if __name__ == '__main__':
    main()