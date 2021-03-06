# Prize Generator
A multi service application to randomly generate a account string and number then award a prize to the account based on some predetermined rules.

An account will add to its prize if:

- the integer part is a multiple of 3, 10 or 7
- the string part contains a f or q
- the string part has repeating characters

a second implementation that can be swapped out will double the users prize.

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
![boarddiagram](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/workflow.PNG)

For use cases, database design and other graphical documentation Lucid boards was used to build these

Lucid boards has many templates and pre-loaded shapes for quick and easy construction of graphical documentaion, I would highly recommend this.
### Design documentation and diagrams
Database table definitions:
![dbdef](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/accounttable.PNG)

Swarm configuration design:
The design uses three nodes in a docker swarm; manager, worker-1 and worker-2, connected to an Ngnix load balancer to mediate user traffic
![fsm](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/swarmconfig.PNG)

Stack configuration:
The stack consists of a front end, service 1, interacting with several back end services; service 2, 3, 4 and the database:
![fsm](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/servicediagram.PNG)

To build the project we use a pipeline consisting of may stages to verify the applicaiton is built correctly:
- Declaritive checlout scm. Clones the git repository to the jenkins machine
- Prerequisites. Installs any prerequisities, new or old, to the jenkins machine
- Test. tests the application to see if working correctly.
- Build images. Builds the services into containers ready for deployment.
- Push. Pushes the images to a repo where the swarm can access them
- Configure. Ansible will now set up the swarm, installing dependencies and connecting the manager and worker nodes of the swarm
- Deploy. the images are pulled from the docker hub repo and deployed as a stack to the swarm
![fsm](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/pipeline.PNG)


### Architecture and software tools used:
Google cloud will be used to host the virtual envinronments and database

MySQL is used for the database logic and storage

The main logic is written in Python

Flask is used to build the web framework of the application

To deploy the application a variety of tools have been used:
- Ansible is used to configure the virtual machines for deployment ensuring all requirements and connections are met
- Docker creates the images for each service, containerising them.
- Using the Docker swarm functionality to deploy across multiple machines
- Jenkins is used to build the application removing downtime and impact to end users
- Nginx is used to balance incoming requests between the nodes of he swarm

A Version Control System is used to manage changes to the application and development, this is used with Git in conjuction with GitHub to host. The Dev branch is used to develop the application while Jenkins is linked to the main branch to host the application. To add a new feature or code when completed and tested, it is merged with the main branch. This allows development to happen while the application is live and ensures zero downtime.

![git](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/pytestcov.PNG)

The PyTest and unit test libraries are used to test the CRUD functions of the application, using white and black box testing methods. The tests have covered all CRUD functions and loading/redirecting of pages:

As shown above a test coverage of 84% has been reached.

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

## Risk assessment:

![ra](https://github.com/JackEMiller/PrizeGenerator/blob/dev2/images/riskassessment.PNG)


## Current Version 1.0.0
### Using the application:
The application is currently live on link: http://35.242.166.72/
