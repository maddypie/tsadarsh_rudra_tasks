import re
from random import randint

import SpeechToText.SpeechToText as SpeechToText


def start_game():
    _welcome_screen()
    record_user_input = SpeechToText.speech_to_text(SECONDS=3)
    user_input = record_user_input.lower()
    patterns = ["rock", "paper", "scissors"]
    comp_choice = get_comp_choice(patterns)
    user_choice = parse_user_input(user_input, patterns)
    if user_choice:
        _display_choices(comp_choice, user_choice)
        win_lose = results(comp_choice, user_choice)
    else:
        _display_user_input_error(user_input)

    output = f"COMPUTER:  {comp_choice}\nYOU: {user_choice}\nRESULT: {win_lose}"
    return output


def _welcome_screen():
    print("Let play this game")
    print("You will be given 3 seconds window to give your input")
    print("You have three options: 'Rock', 'Paper', or 'Scissor'. Choose one")
    print("I'm listening...")


def get_comp_choice(choices: list):
    choice = choices[randint(0, len(choices)-1)]
    return choice


def parse_user_input(user_input: str, choices: list):
    for pattern in choices:
        if re.search(pattern, user_input):
            user_choice = pattern
            return user_choice
    return


def _display_choices(comp_choice: str, user_choice: str):
    print("COMPUTER:", comp_choice)
    print("YOU:", user_choice)
    return


def _display_user_input_error(user_input: str):
    msg = "I couldn't catch you. Try again."
    print(msg)
    return msg


def results(c, i):
    ROCK = "rock"
    PAPER = "paper"
    SCISSOR = "scissors"
    WIN = "Yay! You WON."
    LOSE = "Oops! You lost this time."

    pos = {(ROCK, PAPER): WIN,
           (ROCK, SCISSOR): LOSE,
           (PAPER, SCISSOR): WIN,
           (PAPER, ROCK): LOSE,
           (SCISSOR, PAPER): LOSE,
           (SCISSOR, ROCK): WIN
           }
    message = pos.get((c, i), "It is a Tie!")
    return message
