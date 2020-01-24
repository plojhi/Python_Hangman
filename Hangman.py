import random
import string

print("H A N G M A N")


def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']

    selected = random.choice(words)
    selected_set = set(selected)
    control_set = set()

    output = "-" * len(selected)
    lives = 8
    while lives > 0:
        print()
        print(output)

        letter = input("Input a letter: ")

        if len(letter) != 1:
                print("You should print a single letter")
                continue

        if letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue

        if letter in selected_set:
            if letter not in output:
                for j in range(len(selected)):
                    if selected[j] == letter:
                        output = output[0:j] + letter + output[(j + 1):len(selected)]
            else:
                print("You already typed this letter")

        else:
            if letter in control_set:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                control_set.add(letter)
                lives -= 1

        if "-" not in output:
            print(output)
            print("You guessed the word!")
            print("You survived!")
            break


    if lives == 0:
        print("You are hanged!")

while True:
    question = input('Type "play" to play the game, "exit" to quit: ')
    if question == "play":
        hangman()
        break
    elif question == "exit":
        break

