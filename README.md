# Space Quiz

Description

![Responsice Mockup](https://res.cloudinary.com/dcydt01ed/image/upload/v1681601846/space_quiz_gehn8l.png)
Visit the live site [Here](https://space-quiz-pp3.herokuapp.com/)


## Contents
- [User Experience](#user-experience)
  - [Site Owner's Goals](#site-owners-goals)
  - [Users Goals](#users-goals)
- [Features](#features)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
  - [](#)
- [Design](#design)
  - [Process Flow](#process-flow)
  - [Colour Pallete](#colour-pallete)
- [Technologies](#technologies)
  - [Language](#language)
  - [Flowchart](#flowchart)
- [Testing](testing)
  - [Functional Testing](#functional-testing)
  - [Manual Testing](#manual-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Validator Testing](#validator-testing)
  - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Resources](#resources)
- [Acknowledgments](#acknowledgments)

## User Experience

  ### Site Owner's Goals
  - 
    
  ### Users Goals
  - 
  
  [🔼 Back to top](#contents)

## Features 

### 

  - 
<p><img src="" width="800px" height="auto"  alt="Nav_bar"></p>

### 

   - 

<p><img src="" width="800px" height="auto"  alt=""></p>

### 

  - 

  <p><img src="" width="300px" height="auto"  alt=""></p>


### 

  - 
<p><img src="" width="800px" height="auto"  alt=""></p>

### 

  - 

<p><img src="" width="800px" height="auto"  alt=""></p>

### 

  - 

<p><img src="" width="800px" height="auto"  alt=""></p>

### 

  - 

<p><img src="" width="800px" height="auto"  alt=""></p>

### 

  - 

<p><img src="" width="800px" height="auto"  alt=""></p>

### Existing Features

  - 

[🔼 Back to top](#contents)

## Design

### Process Flow

- Flowchart to demonstrate the actions that take place while using the app.

<p><img src="" width="700px" height="auto"  alt="Flowchart"></p>


### Colour Pallete

  - 

<p><img src="" width="300px" height="auto"  alt="Colour-pallete"></p>

[🔼 Back to top](#contents)

## Technologies

#### Language
  - Python

#### Flowchart
  - Flowchart was created using lucidchart from https://www.lucidchart.com/pages/.

[🔼 Back to top](#contents)

## Testing 

### Functional Testing

<table>
  <tr>
    <th></th>
    <th>Test</th>
    <th>Completed Succsessfully</th>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>
    <tr>
    <td></td>
    <td></td>
    <td></td>
    </tr>
</table>

### Manual testing

- Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Lighthouse Testing

I generated a lighthouse report to check my performance and the scores are good. The lower score for the SEO is caused by the lack of meta description.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681602070/lighthouse_gny4rb.png" width="400px" height="auto"  alt="Lighthouse"></p>

### Validator Testing 

The [PEP8CI](https://pep8ci.herokuapp.com/) Validator Service was used to validate every Python file in the project to ensure there were no syntax errors in the project.

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1681602378/pep8ci_ofpeat.png" width="800px" height="auto"  alt=""></p>

- No errors or warnings were found during the last testing of the code in PEP8CI.


### Bugs

- Fixed Bug

I was struggling to get the ten random questions from the data dictionary. Only one random question was showing.
It took me awhile to figure it out that there was an indentation mistake which wasn't shown in pip8ci.

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
- [How to clear the console:](https://appdividend.com/2022/06/03/how-to-clear-console-in-python/#:~:text=For%20the%20Windows%20system%2C%20to,('cls'))
- [How to add Python sleep - for timing the texts:](https://realpython.com/python-sleep/)
- [Simple quiz plus flowchart Python](https://www.youtube.com/watch?v=LXSvzUimHBk)


[🔼 Back to top](#contents)

## Acknowledgments

- My Mentor for continious helpful feedback.
- I would like to thank the Code Institute tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank my husband, for believing in me, and for the moral support; it kept me going during periods of self-doubt.


[🔼 Back to top](#contents)


