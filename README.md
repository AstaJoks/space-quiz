# Space Quiz

Description

Space Quiz is a Project Portfolio 3 for Code Institute Full Stack Software Development. This project is a command line application built with Python. 
Made with passion for anyone interested in space, astronomy and anything related to it. Users test their knowledge of Outer Space by answering 10 multiple questions.

![Responsice Mockup](https://res.cloudinary.com/dcydt01ed/image/upload/v1681601846/space_quiz_gehn8l.png)
Visit the live site [Here](https://space-quiz-pp3.herokuapp.com/)


## Contents
- [User Experience](#user-experience)
  - [Project Goals](#project-goals)
  - [User Expectations](#user-expectations)
  - [Users Stories](#users-stories)
- [Features](#features)
  - [Main Page and Intro Message](#main-page-and-intro-message)
  - [Instructions](#instructions)
  - [Questions](#questions)
  - [Final Score](#final-score)
  - [High Score Table](#high-score-table)
  - [Play Again](#play-again)
  - [Results Worksheet](#results-worksheet)
  - [Storage Data](#storage-data)
  - [Data Model](#data-model)
- [Design](#design)
  - [Colours](#colours)
  - [Process Flow](#process-flow)
  - [Accessibility](accessibility)
- [Technologies](#technologies)
  - [Language](#language)
  - [Frameworks and Programs used](#frameworks-and-programs-used)
- [Testing](testing)
  - [Functional Testing](#functional-testing)
  - [Manual Testing](#manual-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [CI Python Linter](#ci-python-linter)
  - [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Resources](#resources)
- [Acknowledgments](#acknowledgments)

## User Experience

  ### Project Goals
  - Provide the user with a fun, engaging and easy to play multiple choice quiz.
  - Provide some visuals with the use of ASCII art and colour to contribute to a positive user experience.
  - Provide an appropriate response to all user inputs and ensure any invalid data is handled appropriately.
  - Accurately keep track of and display the user’s score clearly at the end of the quiz.
  - Keep good UX principles regarding layout/colours/interaction.

  ### User Expectations
  - Able to quickly understand what the purpose of the site is.
  - Find info/rules if needed.
  - Every interaction has feedback.
  - Get more info about question/answer, right or wrong.
  - Get name on/see the high scores.
  - No errors with the game logic.

  ### Users Stories
  - To play a fun and easy to use quiz.
  - Clear instructions on how to use the quiz.
  - To test my knowledge of Outer Space.
  - To be informed when my input is invalid, and to be given the opportunity to correct any invalid input without interrupting the flow of the quiz.
  - To be able to read the application output clearly.
  - To see my total score out of ten at the end of the quiz.
  - To be able to easily repeat the quiz if I want to try again.
  
  [🔼 Back to top](#contents)

## Features 

### Main Page and Intro Message
<br/>

*Project Goal - Provide some visuals with the use of ASCII art and colour to contribute to a positive user experience.*

 - As design and layout features in command line applications are restrictive, I decided to use pyfiglet for converting regular text in to different forms
of ASCII art for LOGO of Space Quiz.
 - And I have used the Python module 'Colorama' throughout the program to add color within the terminal.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681683715/main_page_y2mvwl.png" width="800px" height="auto"  alt="Main Page"></p>

### Instructions
<br/>

*As a user I want clear instructions on how to use the quiz.*

 - Once the user has entered their name, they are given a personalised welcome message, and are presented with a short description and simple instructions for the quiz.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681684462/instructions_l0psxn.png" width="800px" height="auto"  alt="Instructions"></p>

 - The user is then asked if they are ready to play the quiz by typing 'y' for yes or 'n' for no. This allows user initiation and control of the logic flow in this stage of the program.
 - If the user types 'y' the quiz will begin and if 'n' is typed a message will appear asking them to type 'y' if they ready to begin, else start the quiz another time.

  <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681684871/start_quiz_validation_petjem.png" width="800px" height="auto"  alt="Start Quiz Validation"></p>

### Questions
<br/>

*Project Goal - Provide the user with a fun, engaging and easy to play multiple choice quiz.*

 - The quiz contains 10(randomly selected out of 20) multiple choice questions of varying difficulty which are iterated randomly each time the program is run.
 - Each correctly answered question scores 1 point, and if the question is answered incorrectly then 0 points are awarded.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681685843/questions_fnjian.png" width="800px" height="auto"  alt="Questions"></p>

 - If the correct answer is selected by the user, they are informed with the output 'That's correct! Well done!' which is colored in green, followed by the next question.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681685717/correct_answer_sfzuyr.png" width="800px" height="auto"  alt="Correct Answer"></p>

 - If an incorrect answer is selected, the output 'Sorry, that's incorrect!' is shown in red.
And show the correct answer.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681685712/incorrect_answer_ybvyg8.png" width="800px" height="auto"  alt="Incorrect Answer"></p>

 - If Incorrect option is selected (not a, b or c) , the output 'Only a, b or c are valid options!'.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681686760/correct_answer_validation_g7w01s.png" width="800px" height="auto"  alt="Option Validation"></p>

### Final Score
<br>

*Project Goal - Accurately keep track of and display the user’s score clearly at the end of the quiz.*

 - Once the user reaches the end of the quiz, he/she is congratulated and told their final score.
 - A message appears informing them that the results worksheet is being updated and the user will be able to see the High Score Table

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681687421/final_score_q6bex7.png" width="800px" height="auto"  alt="Final Score"></p>

### High Score Table

 - Once the results worksheet updated, the app shows the High Score table, which displays name and the five highest scores.
 - The user is also asked if they would like to play again, by typing 'y' for yes or 'n' for no.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681687989/high_score_table_dfhsrb.png" width="800px" height="auto"  alt="High Score Table"></p>

### Play Again

 - If the user type 'y' the quiz starts again.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681688541/try_again_algrem.png" width="800px" height="auto"  alt="Try again Yes"></p>

 - If 'n' is typed, a message thanks the user for playing and informs that the quiz has ended.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681688993/no_xdd14o.png" width="800px" height="auto"  alt="Try again No"></p>

- If invalid option is typed, a message appears informing that only Y/N options are valid.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681688999/yes_no_gj94js.png" width="800px" height="auto"  alt="Invalid option"></p>

### Results Worksheet

  - This Google sheet contains all the users who have completed the quiz along with the score they achieved.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681689734/results_emmnvh.png" width="400px" height="auto"  alt="Results Worksheet"></p>

### Storage Data

 - I have used a Google sheet to save the player's name and score. This sheet is connected to the code through the Google Drive and Google Sheet API by the Google Cloud Platform. This method allows me to send and receive data as I had access to the Google Sheet API credentials. I also added in the Config Vars to these credentials when I was deploying the project in Heroku. As this is sensitive data, I had to add the creds.json in the Git ignore file. This would ensure that these credentials are not pushed to the repository.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681757347/storage_data_hmfdiy.png" width="600px" height="auto"  alt="Storage Data"></p>

### Data Model

 - I used a dictionary in this programme to store the question and answer data for the quiz.
 I have written the code in a way that means additional questions can be added to the dictionary in the future, without having to amend any other code.


[🔼 Back to top](#contents)

## Design

### Colours

  - The colours in the quiz are supplied by the Python Colorama Model.

### Process Flow

- Flow chart to demonstrate the actions that take place while using the app.

   - Part 1 of 2 - Run Program

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681819547/SpaceQuiz_Flowchart_part_1_of_2_ys2leq.png" width="1000px" height="auto"  alt="Flowchart part 1 of 2"></p>

  - Part 2 of 2 -  Quiz Begins

  <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681819552/part_2_of_qgv0wb.png" width="1000px" height="auto"  alt="Flowchart part 2 of 2"></p>

 ### Accessibility

 - The app provides feedback to the user at various stages to instruct them if they have made an error, for example, if they do not enter a name at the beginning, they are instructed to enter a name to proceed.

[🔼 Back to top](#contents)

## Technologies

#### Language
  - Python: to develop the program.

#### Python Modules
  - [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) - to clear the screen.
  - [time](https://pypi.org/project/time/) - to add pauses at certain points during the quiz.
  - [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - to select the random questions from the data dictionary.
  - [math](https://docs.python.org/3/library/math.html) - to get 10 random questions out of 20.
  - [gspread](https://pypi.org/project/gspread/) for tracking users names and scores.
  - [google.oauth2.service_accoun](https://google-auth.readthedocs.io/en/stable/index.html): credentials used to validate credentials and grant access to Google service accounts
  - [pyfiglet](https://pypi.org/project/pyfiglet/) for converting regular text in to different forms of ASCII art.
  - [colorama](https://pypi.org/project/colorama/) for adding a colour to the different parts of quiz.

#### Frameworks and Programs used

This Project used:

  - [Git](https://git-scm.com/) for version control.
  - [GitHub](https://github.com/) to store the project files.
  - [Heroku](https://www.heroku.com/about) to deploy the website.
  - [Lucidchart](https://www.lucidchart.com/pages/) to create the flow chart.

[🔼 Back to top](#contents)

## Testing 

### Functional Testing

<table>
  <tr>
    <th>Test</th>
    <th>Completed Succsessfully</th>
  </tr>
  <tr>
    <td>The terminal has no issues and is working properly</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The input for name has the right behaviour and shows the user an alert if the input is empty</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The welcome message and game rules appear without any issues after the user submits their name</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The option to press 'y' to start a game is running well and shows the user an alert if the input is invalid</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The quiz questions run without any issues and as expected(10 out of 20 questions randomly run when a new quiz starts)</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>Correct/Incorrect answer message appears without any issues and shows the user an alert if the input is invalid</td>
    <td>Yes</td>
  </tr>
   <tr>
    <td>The score appears after correct answer as expected</td>
    <td>Yes</td>
  </tr>
   <tr>
    <td>The correct answer appears if the user answers incorrectly</td>
    <td>Yes</td>
  </tr>
   <tr>
    <td>The final score runs without any issues and as expected</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The score worksheet updating without any issues and as expected</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The High Score Table shows the five highest scores</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The option to press 'y' to start a quiz again is running well and shows the user an alert if the input is invalid</td>
    <td>Yes</td>
  </tr>
  <tr>
    <td>The quiz restarts at the questions section(not at the intro message) if the user decides to run it again</td>
    <td>Yes</td>
  </tr>
</table>


### Manual testing

I have carried out the following manual tests throughout the development process:

  - Given invalid input at each input stage to check invalid data is dealt with in the way I expected.
  - Tested in my local terminal and the deployed Heroku terminal.
  - Asked friends and family to play the quiz to check that it works on various browsers and that the quiz functionality is understandable.


### Lighthouse Testing

I generated a lighthouse report to check my performance and the scores are good. The lower score for the SEO is caused by the lack of meta description.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681602070/lighthouse_gny4rb.png" width="600px" height="auto"  alt="Lighthouse"></p>


### CI Python Linter

No errors or warnings were found during the last testing of the code in [CI Python Linter](https://pep8ci.herokuapp.com/).

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681602378/pep8ci_ofpeat.png" width="800px" height="auto"  alt=""></p>


### Bugs

- Fixed Bug

   - I was struggling to get the ten random questions from the data dictionary. Only one random question was showing.
It took me awhile to figure it out that there was an indentation mistake which wasn't shown in PIP8CI.

- Known Bugs

   - The emojis (smiley faces after correct/wrong answer in the quiz) don't always render properly for user on Mozilla Firefox . I did not manage to find a solution to fix this.

[🔼 Back to top](#contents)


## Deployment

### Creating the Repository

I have used the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) 
for creating a terminal where my Python code will generate its output. The steps were as follows:

- Click the Use this template button
- A New Repository page will appear, write a Repository name and a short description and press Create repository from template
- Press the green Gitpod button to create your project workspace and start developing your website

### Deploying on Heroku

- Create an account and login into Heroku website
- Click "New -> Create new app" button
- Insert your app's Name and Choose your region then click the "Create App" button
- Into the Settings tab go to "Config vars" section and click "Reveal Config Vars"
- Enter the PORT in the KEY section and 8000 for its value, then click "Add"
- Enter the CREDS in the KEY section and add all the files from the creds.json file for its value, then click "Add"
- Go to "Buildpacks" section and click "Add buildpack"
- Firstly add the Python buildpack then NodeJs
- Into the Deploy tab go to "Deployment method" and select Github
- After that go to "App connected to GitHub" and look for your GitHub repository name to link it
- You can now choose to either manually or automatically deploy your app to Heroku
- With automatic deploys enabled, Heroku will build a new version of the app each time a change has been
  pushed to the repository
- Manual deploys means your app will be updated only when you manually click to deploy it
- When the deploying is finished, a link will be provided to you for accessing your app

The live link can be found [here](https://space-quiz-pp3.herokuapp.com/)

### Forking the Repository

You can fork the repository by following these steps:

- Go to the GitHub repository.
- Locate the Fork button on the top-right corner of the page and click on it.
- Select an owner for the forked repository and give it a name.
- Add a description of the repository if you want to.
- Choose whether to copy only the default branch or all of the branches to the new fork (Only the default branch is copied by default).
- Click Create fork.

### Cloning the Repository

You can clone the repository by following these steps:

- Log into GitHub.
- Find the repository you want to clone.
- To the left of the big green 'Gitpod' button, click the 'Code' dropdown menu.
- Copy the HTTPS or SSH address as required.
- Open Git Bash.
- Set up your new directory.
- Type "git clone the_SSH_or_https_address".
- Hit enter and the code will be cloned.

[🔼 Back to top](#contents)

## Credits 

### Content

- [Food of Japan Quiz](https://github.com/cornishcoder1/Food_of_Japan_Quiz) - quiz intro and run quiz functions based on project by Leah Fisher.
- [Love Sandwiches ](https://learn.codeinstitute.net/.ie) - exporting results functionality based on Love Sandwiches Walkthrough project by Code Institute.

### Resources

- [Code Institute](https://codeinstitute.net/ie/)
- [Readme](https://readme.so/)
- [Simple Multiple Choice Quiz Game in Python](https://www.youtube.com/watch?v=mxDeSkuLBeY&t=372s)
- [W3Schools - Python](https://www.w3schools.com/python/)
- [How to clear the console](https://appdividend.com/2022/06/03/how-to-clear-console-in-python/#:~:text=For%20the%20Windows%20system%2C%20to,('cls'))
- [How to add Python sleep - for timing the texts](https://realpython.com/python-sleep/)
- [Simple quiz plus flowchart Python](https://www.youtube.com/watch?v=LXSvzUimHBk)


[🔼 Back to top](#contents)

## Acknowledgments

- Big thank you for my Mentor for continious helpful feedback.
- I would like to thank my husband, for believing in me, and for the moral support. It kept me going during periods of self-doubt.


[🔼 Back to top](#contents)


