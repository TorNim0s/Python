"""
Not exacly as you asked
made a few changes what do u think?
"""

import random

HANGMAN_PHOTOS = {0: "x-------x",
                  1: "x-------x\n|\n|\n|\n|\n|",
                  2: "x-------x\n|       |\n|       0\n|\n|\n|",
                  3: "x-------x\n|       |\n|       0\n|       |\n|\n|",
                  4: "x-------x\n|       |\n|       0\n|      /|\\\n|\n|",
                  5: "x-------x\n|       |\n|       0\n|      /|\\\n|      /\n|",
                  6: "x-------x\n|       |\n|       0\n|      /|\\\n|      / \\\n|"}

def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    if (len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed not in old_letter_guessed):
        old_letter_guessed += [letter_guessed]
        print (old_letter_guessed)
    else :
        notvalidletter(old_letter_guessed)
    return old_letter_guessed

def notvalidletter(old_letters):
    print("X")
    print(" -> ".join(sorted(old_letters)))

def show_hidden_word(secret_word, old_letters_guessed):
    info = ""
    for item in secret_word:
        same = False
        for work in old_letters_guessed:
            if item == work:
                info += item
                same = True
        if (same == False):
            info+="_"
    print(info)

def checkwin(secret_word, old_letters_guessed):
    counter = 0;
    for item in secret_word:
        for work in old_letters_guessed:
            if item == work:
                counter += 1
    return counter == len(secret_word)

def print_hangman(num_of_tries):
    global HANGMAN_PHOTOS
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path):
    with open(file_path, "r") as file:
        words_list = file.read().split("\n")
        return random.choice(words_list)

def main():
    print("Wellcome to hangman game")
    file_path = input("Please enter path to words list file: ")

    old_letters = []

    num_of_tries = 0
    print_hangman(num_of_tries)

    secret_word = choose_word(file_path)

    while (not checkwin(secret_word, old_letters)):
        newletter = input("Enter a valid letter: ")

        if newletter not in secret_word and newletter not in old_letters:
            num_of_tries += 1

        old_letters = try_update_letter_guessed(newletter, old_letters)

        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters)

        if num_of_tries == 6:
            print("LOSE")
            break
    if num_of_tries < 6:
        print("Winner!!!")

if __name__ == "__main__":
    main()
