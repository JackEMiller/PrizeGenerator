# Club Forum
A forum for a martial arts club to record members, techniques and details of classes.

## Software Design:
### Project management:
This project has used Azure boards to manage the tasks performed to build the software:

[![Board Status](https://dev.azure.com/JMiller10074/afdffd25-69bf-4fba-9fbd-056a02328592/29fd3513-e2ad-42c4-bc9e-153b38e4d8d1/_apis/work/boardbadge/4afc58ad-4793-4732-bbd2-9e2219edcea5)](https://dev.azure.com/JMiller10074/afdffd25-69bf-4fba-9fbd-056a02328592/_boards/board/t/29fd3513-e2ad-42c4-bc9e-153b38e4d8d1/Microsoft.RequirementCategory)

A sample cut of the board:
![boardcut](https://github.com/JackEMiller/ClubForum/blob/main/images/azureb1.PNG?raw=true)

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
### References:
- QA community courseware (only viewable by QA community members)
- Flask documentation 
- Flask tutorials
- Google cloud documentaion
- Dara Oladapo

For a full breakdown please download this presentation:

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
The application is currently live on link: http://34.121.73.96:5000/

You will see:

![login](https://github.com/JackEMiller/ClubForum/blob/main/images/login.PNG?raw=true)

If you do not have an account click the link to "sign up here"

This will forward you to the signup page where you can create an account. Enter a username and password and click submit. If a red message saying "success" appears navigate back to the log in page and log in.

![signup](https://github.com/JackEMiller/ClubForum/blob/main/images/signup.PNG?raw=true)

This will direct you to the view page. The data for Members and Techniques are shown here along with the input for said tables. To submit data; add entrys to each respective field and press submit.

![view](https://github.com/JackEMiller/ClubForum/blob/main/images/view.PNG?raw=true)

Here we will add a member called "Jack":

![addmember](https://github.com/JackEMiller/ClubForum/blob/main/images/submitmember.PNG?raw=true)

After pressing submit the tables will be updated to show any new data:

![deletemember](https://github.com/JackEMiller/ClubForum/blob/main/images/membertable1.PNG?raw=true)

The links to the side of each entry on the table are to; delete the entry, update the entry and to view any classes the entry is related to. If we click "update" we will be forwarded to a new page where we can update the users information, in this case we will change "Jack" to "James":

![updatemember](https://github.com/JackEMiller/ClubForum/blob/main/images/memberupdate.PNG?raw=true)

After pressing submit we will be redirected back to the view page where the change is reflected in the Members table:

![updatemember2](https://github.com/JackEMiller/ClubForum/blob/main/images/membertable2.PNG?raw=true)

Now we will add a class, the class form on the rightmost side is used. Select the date and the number of members and techniques to add to this classe, in this case we will choose one for each:

![addclass](https://github.com/JackEMiller/ClubForum/blob/main/images/classinput.PNG?raw=true)

This will take us to a new page where we can select which member and technique to add to the class:

![addclass2](https://github.com/JackEMiller/ClubForum/blob/main/images/classinput2.PNG?raw=true)

After clicking submit we are taken to the view classes page, where the new class is added to the table:

![viewclass2](https://github.com/JackEMiller/ClubForum/blob/main/images/classview.PNG?raw=true)

We will now update the entry and add another technique to the class, the link "update" in the actions column is used. This brings us to the update class page:

![viewclass2](https://github.com/JackEMiller/ClubForum/blob/main/images/classupdate.PNG?raw=true)

To add another row to the technique section click the "Add another technique" link:

![viewclass2](https://github.com/JackEMiller/ClubForum/blob/main/images/classupdate2.PNG?raw=true)

Select another technique to add then click submit. This will redirect us to the view page where the change is reflected in the table:

![viewclass2](https://github.com/JackEMiller/ClubForum/blob/main/images/classupdate3.PNG?raw=true)