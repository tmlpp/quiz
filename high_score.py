#!/usr/bin/python

import pickle
import os

def create_hs_file():
    """Create the 'high_scores.dat' file if it doest's exist."""
    try:
        if not os.path.exists("high_scores.dat"):
            with open("high_scores.dat", "wb") as hs_file:
                hs = [[0, "n/a"]] * 10
                pickle.dump(hs, hs_file)
            print("High scores file was succesfully created!")
            return True
        else:
            return True
    except PermissionError:
        print("Unable to create the high scores file. High score functionality disabled.")
        return False



def save_high_score(score, name):
    """Save the player's result tu high scores list if the result is good enough"""

    # create the file if doesn't exist
    # if more than 10, pop the last one
    # if 
    try:
        with open("high_scores.dat", "rb+") as hs_file:
            hs = pickle.load(hs_file)
            for i in range(len(hs)):
                if score <= hs[i][0]:
                    hs.insert(i, [score, name])
                    break
                else:
                    if i == 9:
                        hs.append([score, name])
                    else:
                        continue
            hs.pop(0)
            pickle.dump(hs, hs_file)
    except PermissionError:
        print("Unable to write to the high scores file.")
        


def show_high_scores():
    """Print the high scores from highscores.txt if it exists"""
    try:
        with open("high_scores.dat", "rb") as hs_file:
            hs = pickle.load(hs_file)
        hs.reverse()
        print()
        print("+++++++++++ HIGH SCORES +++++++++++")
        print("## ... NAME ..................SCORE")
        for index, hs_line in enumerate(hs, 1):
            print(index, (5 - len(str(index))) * ".", hs_line[1], (25 - len(str(hs_line[1]))) * ".", hs_line[0])
    except FileNotFoundError:
        print("Unable to find the high score file.")


if __name__ == '__main__':
    print("high_score.py is a module for quiz.py and not supposed to be run on its own. Exiting...")
    
