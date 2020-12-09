#!/usr/bin/python

import random
import sys
from high_score import *

QUESTIONS = 10

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
                    return
                else:
                    print("Please use numbers 1–4 to answer. Or choose 0 to end the game.")
                    continue
        if str(answer) == questions[i].get("correct"):
            print("CORRECT!\n")
            score += 1
        else:
            print("Unfortunately that's incorrect.")
            print("The correct answer was {}\n".format(questions[i].get(questions[i].get("correct"))))

    if hs_enabled == True:
        save_high_score(score, name)


def menu():
    while True:
        print()
        print("What do you want to do?")
        choice = input("1: Play a new game\n2: Show high score\n0: Quit\n")
        if choice == "1":
            play_game(name)
        elif choice == "2":
            show_high_scores()
        elif choice == "0":
            print("Thank you for playing! Bye!")
            sys.exit(0)
        else:
            continue


if __name__ == '__main__':
    hs_enabled = create_hs_file()
    while True:
        name = input("Enter your name: ")
        if len(name) > 20:
            print("Name can't be over 20 characters")
            continue
        else:
            break
    print()
    print("Hello, " + name + "!")
    print("Welcome to a quiz game!")
    menu()
