#!/usr/bin/python

import random
import sys

QUESTIONS = 10

# hs = [["Teemu", 32], ["Sanna", 12], ["Hanna", 20], ["Foo", 12], ["Katariina", 2], ["Teemu", 32], ["Sanna", 12], ["Hanna", 20], ["Foo", 12], ["Katariina", 2]]
# names = ["Foo", "Sami", "Katariina", "Jo"]

# for i in range(len(hs)):
#     print(str(i + 1), hs[i][0], (25 - len(hs[i][0])) * ".", str(hs[i][1]))
#     # print(hs[i][1] + 25 - len(hs[i][0]) * ".")

# foo = ["Foo", "Bar", "Baz", "Foobar"]

# print(foo)

# foo.insert(2, "Foobaz")

# print(foo)

def save_high_score(name, score):
    """Save the player's result tu high scores list if the result is good enough"""

    # create the file if doesn't exist
    # if more than 10, pop the last one
    # if 
    try:
        with open("highscores.txt", "r+") as f:
            highscores = f.readlines()
            print("dbg: just after reading the file, length of highscores is", str(len(highscores)))
            highscores.insert(3, name + "\n")
            print("dbg: after inserting, the length of highscores is", str(len(highscores)))
            # print(len(highscores))
            if len(highscores) > 10:
                highscores.pop()
            print("dbg: after possible popping the length of highscores is", str(len(highscores)))
            f.seek(0)
            f.writelines(highscores)
    except PermissionError:
        print("oops")
        


def show_high_scores():
    """Print the high scores from highscores.txt if it exists"""
    try:
        with open("highscores.txt", "r") as f:
            print("+++ HIGH SCORES +++")
            print(f.readlines())
    except FileNotFoundError:
        print("Can't show the high scores because highscores.txt wasn't found.")
        print("This probably means no one has played the game before.")


def prepare_questions():
    questions = pick_questions()



def pick_questions():
    """
    Randomly choose questions from the questions.txt file.
    
    The number of questions to pick is defined by QUESTIONS
    """

    keys = ["question", "1", "2", "3", "4", "correct"]
    questions = []
    with open("questions.txt", "r") as f:
        all_questions = f.readlines()
        numbers = random.sample(range(len(all_questions)), QUESTIONS)
        for i in numbers:
            question = all_questions[i].split("|")
            for i in range(len(question)):
                question[i] = question[i].strip()
            questions.append(dict(zip(keys, question)))
            # questions.append(dict(zip(keys, all_questions[i].split("|"))))
    return questions


def play_game(arg):
    questions = pick_questions()
    score = 0

    for i in range(QUESTIONS):
        print("### QUESTION {} ###".format(i + 1))
        print(questions[i].get("question") + "?")
        for j in range(1, 5):
            print(str(j) + ".", questions[i].get(str(j)))
        while True:
            try:
                answer = int(input("Answer: "))
            except ValueError:
                print("Please use numbers 1–4 to answer. Or choose 0 to end the game.")
                continue
            else:
                if answer > 0 and answer <= 4:
                    break
                elif answer == 0:
                    print("Game ended. Returning to menu.")
                else:
                    print("Please use numbers 1–4 to answer. Or choose 0 to end the game.")
                    continue
        if str(answer) == questions[i].get("correct"):
            print("CORRECT!\n")
            score += 1
        else:
            print("Unfortunately that's incorrect.")
            print("The correct answer was {}\n".format(questions[i].get(questions[i].get("correct"))))

    save_high_score(score)


def menu():
    while True:
        print("What do you want to do?")
        choice = input("1: Play a new game\n2: Show high score\n0: Quit\n")
        if choice == "1":
            play_game(name)
        elif choice == "2":
            show_high_scores()
        elif choice == "3":
            pick_questions()
        elif choice == "0":
            print("Thank you for playing! Bye!")
            sys.exit(0)
        else:
            continue


if __name__ == '__main__':
    print("Welcome to a quiz game!")
    name = input("Enter your name: ")
    print()
    print("Hello, " + name + "!")
    menu()
