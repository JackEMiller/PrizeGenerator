# Prize Generator
A multi service application to randomly generate a account string and number then award a prize to the account based on some predetermined rules.

An account will add to its prize if:

- the integer part is a multiple of 3, 10 or 7
- the string part contains a f or q
- the string part has repeating characters

## Software Design:
### Project management:
The project uses a sstack configuraiton composed of a front end and back end service.

The front end acts as a single service to provide an interface for the user to communicate with the back end.

The back end consists of three different services:
- The first service generates the string part of the account
- the second service generates the integer part of the account
- the third service generates the prize

The stack is then deployed onto a swarm of virtual machines using docker to manage them.

This project has used Azure boards to manage the tasks performed to build the software:

[![Board Status](https://dev.azure.com/JMiller10074/afdffd25-69bf-4fba-9fbd-056a02328592/29fd3513-e2ad-42c4-bc9e-153b38e4d8d1/_apis/work/boardbadge/4afc58ad-4793-4732-bbd2-9e2219edcea5)](https://dev.azure.com/JMiller10074/afdffd25-69bf-4fba-9fbd-056a02328592/_boards/board/t/29fd3513-e2ad-42c4-bc9e-153b38e4d8d1/Microsoft.RequirementCategory)

Azure Boards cumulative flow diagram:
![boarddiagram](https://github.com/JackEMiller/ClubForum/blob/main/images/workflow.PNG?raw=true)

For use cases, database design and other graphical documentation Lucid boards was used to build these

Lucid boards has many templates and pre-loaded shapes for quick and easy construction of graphical documentaion, I would highly recommend this.
### Design documentation and diagrams
Database table definitions:
![dbdef](https://github.com/JackEMiller/ClubForum/blob/main/images/dbdefs.PNG?raw=true)

Database entity relationship diagram:
As you can see the Members and Techniques tables have a many-many relationship with the Classes table. So two intersection tables have been made.
![dberd](https://github.com/JackEMiller/ClubForum/blob/main/images/dberd.PNG?raw=true)

Use Case:
Two users will be present, admin and member. A member cannot use the database manipulation functions and can only view data.
![usecase](https://github.com/JackEMiller/ClubForum/blob/main/images/usecase.PNG?raw=true)

GUI design:
The design is based on a Finite State Machine. and routes between each state is defined as below:
![fsm](https://github.com/JackEMiller/ClubForum/blob/main/images/fsm.PNG?raw=true)

### Architecture and software tools used:
Google cloud will be used to host the virtual envinronment

MySQL is used for the database logic and storage

The main logic is written in Python

Flask is used to build the web framework of the application

To deploy the application a variety of tools have been used:
- Ansible is used to configure the virtual machines for deployment ensuring all requirements and connections are met
- Docker creates the images for each service, containerising them.
- Using the Docker swarm functionality to deploy across multiple machines
- Jenkins is used to build the application removing downtime and impact to end users
- Nginx is used to balance incoming requests between the nodes of he swarm

A Version Control System is used to manage changes to the application and development, this is used with Git in conjuction with GitHub to host. The Dev branch is used to develop the application while Jenkins is linked to the main branch to host the application. To add a new feature or code when completed and tested, it is merged with the main branch. This allows development to happen while the application is live and ensures zero downtime:

![git](https://github.com/JackEMiller/ClubForum/blob/main/images/merge.PNG?raw=true)

The PyTest and unit test libraries are used to test the CRUD functions of the application, using white and black box testing methods. The tests have covered all CRUD functions and loading/redirecting of pages:

![tests](https://github.com/JackEMiller/ClubForum/blob/main/images/testcomplete.PNG?raw=true)

As shown above a test coverage of 93% has been reached.

## Other tools and references:
### Full list of tools used:
- Pycharm
- Google cloud
- MySQL
- Git
- Git Bash
- Git Hub
- Azure boards
- Flask
- Python and various Python packages (full details in design diary *insert link here*)
- Jenkins
- HTTP
- CSS
- Jinja
- Google Chrome
- Linux
- Docker
- Jenkins
- Nginx

### References:
- QA community courseware (only viewable by QA community members)
- Flask documentation 
- Flask tutorials
- Jenkins documentation
- Docker documentation
- Google cloud documentaion
- Dara Oladapo
- Harry 

## License:
This product is licensed under the MIT license

## Risks involved
- Anyone can become and admin and edit the database
- Anyone can access the platform
- Hosting is done via GCP, if all the credits are spent the application will not be running
- There is no backup database, if the database is down the application fails
- VM isn't scaled if more people access it than determined, they will not be able to connect

## Current Version 1.0.0
### Using the application:
The application is currently live on link: http://35.242.166.72/