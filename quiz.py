#!/usr/bin/python

import random
import sys

# hs = [["Teemu", 32], ["Sanna", 12], ["Hanna", 20], ["Foo", 12], ["Katariina", 2], ["Teemu", 32], ["Sanna", 12], ["Hanna", 20], ["Foo", 12], ["Katariina", 2]]
# names = ["Foo", "Sami", "Katariina", "Jo"]

# for i in range(len(hs)):
#     print(str(i + 1), hs[i][0], (25 - len(hs[i][0])) * ".", str(hs[i][1]))
#     # print(hs[i][1] + 25 - len(hs[i][0]) * ".")

# foo = ["Foo", "Bar", "Baz", "Foobar"]

# print(foo)

# foo.insert(2, "Foobaz")

# print(foo)

def print_highscore(arg):
    pass

def show_highscore(arg):
    pass

def pick_questions():
    """Randomly choose 10 questions from the questions.txt file."""
    keys = ["question", "1", "2", "3", "4", "correct"]
    questions = []
    numbers = []
    with open("questions.txt", "r") as f:
        all_questions = f.readlines()
        for i in range(10):
            number = random.randint(1, len(all_questions))
            while number in numbers:
                number = random.randint(1, len(all_questions))
                continue
            numbers.append(number)
            questions.append(dict(zip(keys, all_questions[number - 1].split("|"))))
    return questions

def play_game(arg):
    pass




def main():
    print("Welcome to a quiz game!")
    while True:
        print("What do you want to do?")
        choice = int(input("1: Play a new game\n2: Show high score\n0: Quit\n"))
        if choice == 1:
            play_game()
            break
        elif choice == 2:
            show_highscore()
        if choice == 0:
            print("Bye!")
            sys.exit(0)


if __name__ == '__main__':
    main()
