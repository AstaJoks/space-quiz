"""
Imports to use gspread for tracking users names and scores
Import time to add pauses at certain points during the quiz
"""

import gspread
from google.oauth2.service_account import Credentials
import time

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
