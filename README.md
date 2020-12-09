# quiz

This is the final exercise for _TTC2030 – Ohjelmoinnin perusteet_ class.

## Installation and running

1. Clone/download the repository
2. Run `quiz.py`

## Features

- Runs a trivia game with 10 random questions read from a file with bunch of questions
- Saves 10 best scores in a binary file
- Player can show the high scores
- Player can end the game at any point by answering "0"

## Notes

- Splitting the code into multiple files probably wasn't necessary in a small program like this, but I split it anyway just for practice. And maybe if I end up continuin developing this it's nice if there's already files split by topic.
- The questions file is rather short. I figured that the point wasn't come up with trivia questions but get the game to work instead. So, the file includes questions enough for picking random ones, but not enough for the game to get very boring after couple of runs.

## Future improvements

Let's imagine this was something someone would want to build on and continue further, some improvements I can think of right away is:

- Telling the player if they made it to the highs scores list at the end of the game
- Switching player / changing name without closing the program
- Different categories of questions
