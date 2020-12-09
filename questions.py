#!/usr/bin/python

import random

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


if __name__ == '__main__':
    print("questions.py is a module for quiz.py and not supposed to be run on its own. Exiting...")
