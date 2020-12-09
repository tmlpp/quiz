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
            # Keys are an easy way to keeep up with what are we printing and what's
            # the correct answer so turn questions into dictionaries
            questions.append(dict(zip(keys, question)))
    return questions


if __name__ == '__main__':
    print("questions.py is a module for quiz.py and not supposed to be run on its own. Exiting...")
