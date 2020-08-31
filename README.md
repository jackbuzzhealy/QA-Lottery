QA-Lottery

This README.md file contains all the relevant information regarding my project up to the ninth week at the QA Consulting Academy.
Links:
Kanban Board: 
https://jackhealy.atlassian.net/secure/RapidBoard.jspa?rapidView=4&projectKey=QL&selectedIssue=QL-7&quickFilter=8

Website:

http://35.246.120.114/ (Manager Node)

http://34.105.216.178/ (Worker Node)

Contents
•	Requirements
•	Architecture
•	Project Tracking 
•	Testing
•	Risk Assessment
•	Known Issues 
•	Future Improvements

Requirements

The purpose of this assignment was to create API service applications with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.  These applications must make http GET and POST requests to communicate data to each other.  The following technologies were used.
•	A Kanban board (using Jira)
•	Clear documentation of the design phase, app architecture and risk assessment
•	A python-based functional application that follows best practices and design principles
•	Test suites for the application, which will include automated tests for validation of the application
•	A front-end website, created using Flask
•	Code integrated into a Version Control System (GitHub) which will be built through a CI server (Jenkins) and deployed (via Docker Swarm) to a cloud-based virtual machine (GCP)
![MoSCoW]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/MOSCOW.PNG)

Architecture

Flow Diagram:

The User can view their lottery numbers, winning numbers, and the prize on service 1.  Once a link is clicked by the user, a GET request is used to retrieve the generated lottery numbers from service 2 and a POST request is then made to service 4 which generates the winning numbers and checks for any matches between both number lists.  Both number lists and number of matches are then sent back to service 1 to be outputted onto the HTML page.  If there are matches, a query is made to the database to retrieve the correct prize which is also outputted onto the HTML page.

For Lightening Ball, once a link is clicked by the user, a GET request is used to retrieve the generated number from service 3 and a POST request is then made to service 4 which generates the winning number and checks if it matches with the user’s number. Both numbers are then sent back to service 1 to be outputted onto the HTML page.  If the numbers match, a query is made to the database to retrieve the prize which is also outputted onto the HTML page.
![Flow Diagram](https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/Flow-Diagram.png)

CI Pipeline

Pictured below is the continuous integration pipeline with the associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process, i.e. programmes can produce code on their local machines and push it to GitHub, which will automatically push the new code to Jenkins via a webhook to be automatically installed on the cloud VM. From there, tests are automatically run, and reports are produced.
![CI Pipeline]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/CI-Diagram.png)

Project Tracking 
Hyperlink showing the full Kanban board is at the top of this file, but screenshots is provided below to show the progress of the project.
![progress1]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/JiraProgress/progress1.PNG)
![progress2]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/JiraProgress/progress2.PNG)
![ progress3]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/JiraProgress/progress3.PNG)

Testing

Risk Assessment 

![RiskAssessment]( https://github.com/jackbuzzhealy/QA-Lottery/blob/master/DesignImages/Risk-Assessment.PNG)

Known Issues 

Improvements which I would like to make include:

•	Docker Swarm to work properly so that the applications can be deployed robustly

•	To add some CSS to improve the usability 

Authors

Jack Healy
