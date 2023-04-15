"""
Import required modules
Import os for clearing screen to help with user experience
Import time to add pauses at certain points during the quiz
Imports to use gspread for tracking users names and scores
Imports pyfiglet for converting regular text in to different forms of ASCII art
Imports clorama for adding a colour to the different parts of quiz
"""
import os
import time
import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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

high_scores = SHEET.worksheet("scores")
scores = high_scores.get_all_values()

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

]


def quiz_intro():
    """
    Quiz intro displays ASCII title text. Gets
    user name, shows instructions and asks user if they are ready to begin.
    """

    ascii_banner = pyfiglet.figlet_format("Space Quiz")
    print(Fore.BLUE + ascii_banner)

    print("WOULD YOU LIKE TO TEST YOUR KNOWLEDGE ABOUT THE OUTER SPACE?")
    time.sleep(1)
    global NAME
    NAME = input("Please type your name and hit the enter key to start:\n")

    # Relaunches quiz intro if no name is entered and user only clicks Enter
    if NAME == "":
        print(f"{Fore.RED}A name is required to take the quiz!")
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
        begin_quiz = input(f"{Fore.RED}Please enter 'y' to begin {NAME}, else "
                           "complete the quiz another time: ")

    if begin_quiz.lower() == "y":
        print(f"{Fore.WHITE}\nOkay, let's start. Good luck!\n")
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
            print(f"{Fore.BLUE}{entry['question']}")

            # this code prints the 3 options for each question
            for key, value in entry['answers'].items():
                print(f"{key}: {value}")

            user_answer = input("answer(a, b or c): \n")
            user_answer = user_answer.lower()
            # to check if the user pick the accepted option a, b or c
            if user_answer not in entry['answers']:
                print(f"{Fore.RED}Only a, b or c are valid options!\n")

        # this code checks if the answer is correct and adds
        # a point to the score
        if user_answer == entry['correct_answer']:
            print(f"{Fore.GREEN}That's correct {NAME}! Well done!\n")
            score = score + 1
            print(f"Your score: {score}")
            print("☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀ ☀")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        # this code displays the correct answer if the user enters
        # the wrong answer
        elif user_answer != entry['correct_answer']:
            print(f"{Fore.RED}Sorry {NAME}, that's incorrect.\n")
            print(f"The correct answer was {correct_answer}.")
            print("✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴ ✴")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

    # the final screen congratulates the user and tells
    # the final score
    print(f"Well done for completing the Space Quiz, {NAME}.\n")
    print(f"Your total score was {score} points out of 10.\n")
    print("Hope you had fun!")
    data = NAME, score
    export_results(data)

# Export results based on Love Sandwiches project by
# Code Institute


def export_results(data):
    """
    This function will export the results of the quiz including
    the user name and final score to the scores worksheet
    """
    print("Updating results worksheet...\n")
    scores_worksheet = SHEET.worksheet("scores")
    scores_worksheet.append_row(data)
    print("Results exported to worksheet successfully")
    time.sleep(1)
    
    print("Showing the HIGH SCORES...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


game_high_scores = [

 # High scores table display
 """
    =====✴=====✴=====✴=====✴=====✴=====✴=====✴=====
                H I G H   S C O R E S
    ===============================================
    \tPOS\tNAME\tSCORE\t
    ===============================================
"""
]


def display_high_scores():
    """
    Displays to the players the 5 best scores
    """
    score_sheet = SHEET.worksheet("scores").get_all_values()[1:]
    for data in score_sheet:
        data[1] = data[1]

    update_data = sorted(score_sheet, key=lambda x: int(x[1]), reverse=True)

    print(f"{Fore.BLUE}{game_high_scores[0]}")
    if len(update_data) < 5:
        count = len(update_data)
    else:
        count = 5

    for i in range(0, count):
        print(f"""
        {i+1}\t{update_data[i][0]}\t  {update_data[i][1]}""")
    print(f"""{Fore.BLUE}\n
    =====✴=====✴=====✴=====✴=====✴=====✴=====✴=====""")


def try_again():
    """
    At the end of the quiz, proposes to try again.
    """
    restart = input("Would you like to try again and beat your score? (Y/N\n")
    if restart.upper() == "Y":
        main()
    if restart.upper() == "N":
        print("Thank you for taking a quiz. Hope to see you again soon.\n")
    else:
        print(f"{Fore.RED}I did not understand.")
        restart = input(f"{Fore.RED}Would you like to try again? (Y/N")


def main():
    """
    Run all program functions
    """
    quiz_intro()
    run_quiz(quiz_data)
    display_high_scores()
    try_again()


main()
