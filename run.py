"""
Import required modules
Imports to use gspread for tracking users names and scores
Import os for clearing screen to help with user experience
Import time to add pauses at certain points during the quiz
"""
import os
import time
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

"""
Google sheets access credentials variables
"""
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('space_quiz')

NAME = ""
SCORE = 0

"""
Dictionary of quiz questions for space quiz
"""
quiz_data = [
    {"question": "1. Which planet is closest to the sun?",
     "answers": {"a": "Mercury",
                 "b": "Mars",
                 "c": "Venus"},
     "correct_answer": "a"},
    {"question": "2. What shape is the Milky Way?",
     "answers": {"a": "Spiral",
                 "b": "Circle",
                 "c": "Squire"},
     "correct_answer": "a"},
    {"question": "3. Which planet is named after the Roman god of war?",
     "answers": {"a": "Earth",
                 "b": "Mars",
                 "c": "Jupiter"},
     "correct_answer": "b"},
    {"question": "4. What is the name of the force which keeps the planets "
                 "in orbit around the sun?",
     "answers": {"a": "Magnetic Force",
                 "b": "Electric Force",
                 "c": "Gravity Force"},
     "correct_answer": "c"},
    {"question": "5. What would you find if you travelled to the centre "
                 "of the solar system?",
     "answers": {"a": "The Black Hole",
                 "b": "The Moon",
                 "c": "The Sun"},
     "correct_answer": "c"},
    {"question": "6. Which planet has a day which lasts eight months?",
     "answers": {"a": "Mars",
                 "b": "Venus",
                 "c": "Earth"},
     "correct_answer": "b"},
    {"question": "7. How many planets are there in the solar system?",
     "answers": {"a": "Nine",
                 "b": "Seven",
                 "c": "Ten"},
     "correct_answer": "a"},
    {"question": "8. How long is one year on Jupiter?",
     "answers": {"a": "3 Earth years",
                 "b": "8 Earth years",
                 "c": "12 Earth years"},
     "correct_answer": "b"},
    {"question": "9. How many moons does Earth have?",
     "answers": {"a": "Just One",
                 "b": "Two",
                 "c": "None"},
     "correct_answer": "a"},
    {"question": "10. Who invented the telescope?",
     "answers": {"a": "Galileo",
                 "b": "Hans Lippershey",
                 "c": "Johannes Kepler"},
     "correct_answer": "b"},
]


def quiz_intro():
    """
    Quiz intro displays ASCII title text and space image. Gets
    user name, shows instructions and asks user if they are ready to begin.
    """

    print(f"""{Fore.YELLOW}{Style.BRIGHT}
   _____                          ____        _     
  / ____|                        / __ \      (_)    
 | (___  _ __   __ _  ___ ___   | |  | |_   _ _ ____
  \___ \| '_ \ / _` |/ __/ _ \  | |  | | | | | |_  /
  ____) | |_) | (_| | (_|  __/  | |__| | |_| | |/ / 
 |_____/| .__/ \__,_|\___\___|   \___\_\\__,_|_/___|
        | |                                         
        |_|                                           
""")
    print(f"""{Fore.BLUE}{Style.BRIGHT}
        ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .

    \n""")

    print("Would you like to test your knowledge on outer space?")
    time.sleep(1)
    global NAME
    NAME = input("Please type your name and hit the enter key:\n")

    # Relaunches quiz intro if no name is entered and user only clicks Enter
    if NAME == "":
        print("A name is required to take the quiz!")
        quiz_intro()
    else:
        print(f"\nWelcome to the Space Quiz {NAME}.\n")
        time.sleep(1)
        print("The quiz consists of ten questions to test your knowledge "
              "about the outer space and solar system.\n")
        time.sleep(1)
        print("The questions are in multiple choice format.\n")
        time.sleep(1)
        print("Options are a, b or c for all questions.\n")
        time.sleep(1)
        print("When prompted, please enter you answer a, b or c and hit the "
              "enter key.\n")
        time.sleep(1)

    # Asks user if they'd like to begin the quiz pulling in the name they have
    # entered above
    begin_quiz = input(f"Are you ready to begin, {NAME}? (y/n): ")

    while begin_quiz != "y":
        begin_quiz = input(f"Please enter 'y' to begin {NAME}, else "
                           "complete the quiz another time: ")

    if begin_quiz.lower() == "y":
        print("\nOkay, let's start. Good luck!\n")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')


# run_quiz function based on project by Leah Fisher
# https://github.com/cornishcoder1/Food_of_Japan_Quiz


def run_quiz(data):
    """
    Loops through the questions and answers in the quiz data dictionary
    """
    score = 0

    for entry in quiz_data:
        user_answer = ""
        correct_answer = entry['correct_answer']

        # this loop repeats the question until the user enters
        # either a, b or c
        while user_answer not in ['a', 'b', 'c']:
            print(f"{entry['question']}\n")
            # this code prints the 3 options for each question
            for key, value in entry['answers'].items():
                print(f"{key}: {value}")

            user_answer = input("answer(a, b or c): \n")
            user_answer = user_answer.lower()
        # to check if the user pick the accepted option
            if user_answer not in entry['answers']:
                print("Only a, b or c will be accepted as answers!\n")
    
        # this code checks if the answer is correct and adds
        # a point to the score
        if user_answer == entry['correct_answer']:
            print(f"That's correct {NAME}! Well done!c\n")
            score = score + 1
            print(f"Your score: {score}")
            print("☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        # this code displays the correct answer if the user enters
        # the wrong answer
        elif user_answer != entry['correct_answer']:
            print(f"Sorry {NAME}, that's incorrect.\n")
            print(f"The correct answer was {correct_answer}.")
            print("✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

quiz_intro()
run_quiz(quiz_data)
