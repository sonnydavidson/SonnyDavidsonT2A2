# SonnyDavidson_T2A2

## Postgresql instruction to set up DB
- Create the DB

CREATE DATABASE eplapp;

- Create the dev user 

CREATE USER eplapp_dev WITH PASSWORD 'benny';

- Grant privileges

GRANT ALL PRIVILEGES ON DATABASE eplapp TO eplapp_dev;

##	R1 - Identification of the problem you are trying to solve by building this particular app.
With this application the main problem that i am looking to solve is that I believe that there is a hole in the market for an application that 
keeps track of player and team stats in details. I am looking to solve this problem by giving this app the ability and the structure to able to support 
new data being added and old data being updated. also with the way the code for this app is designed it would make it very simple to add new data types
and seacrh parameters in the future to track more statistics.

## R2 -	Why is it a problem that needs solving ?
The reason that i am solving this problem is because an application like this would hugly help scouts and 
coaches track the performance of players and other teams. This would be extremely useful when it comes to signing new players and also doing player
performance reviews. Thus this application would make the jobs of scouts and coaches a lot easier and they would also become efficient because 
they would have access to all possible data points involving each player.

## R3 - Why have you chosen this database system. What are the drawbacks compared to others?
The databse systems I have chosen to use for this application is SQL. One of the disadvantages to SQL is that it uses a lot of processing power and can become bogged down quite easily. It also doesnt handle queries in high volume and also does not handle large amounts of data very well opposed to some of
the other databse syetms avaliable.

## R4 - Identify and discuss the key functionalities and benefits of an ORM
The key functionalities of an ORM ( Object-relational-mapper ) is that it alows you to write queries using the object-oriented paradigm of your preferred programming language. The benefits of using an ORM are you get to write in the language you are already using, they allow you to connect to the database server, they can help you generate querys to use on your database and they help with fetching the data and serializing it if necessary.


## R5 - Document all endpoints for your API
### Register
- HTTP request verb: POST
- Required data if applicable: Name, email, phone number, favourite team and password
- Expected response data: UserSchema
- Authentication methods if applicable: n/a

### Login
- HTTP request verb: POST
- Required data where applicable: The email address and password in JSON format
- Expected response data: JWT Token in JSON format
- Authentication methods where applicable: username and hashed password is checked with the database

### Full table 
- HTTP request verb: get
- Required data where applicable:
- Expected response data: The full table in oder from highest Pts to lowest
- Authentication methods where applicable: 

### Delete a team 
- HTTP request verb: Delete
- Required data where applicable: The teams name you want to delete
- Expected response data: A message confirming which team has been deleted 
- Authentication methods where applicable: JWT Token and admin role

### Update a team 
- HTTP request verb: PUT / PATCH
- Required data where applicable: The teams name you want to delete
- Expected response data: A message confirming which team has been deleted 
- Authentication methods where applicable: JWT Token and admin role

### Add a new team 
- HTTP request verb: POST
- Required data where applicable: position, team, MP, W, D, L, Pts, GF, GA and GD
- Expected response data: 
- Authentication methods where applicable: JWT Token and admin role

### Full list of players 
- HTTP request verb: GET
- Required data where applicable: 
- Expected response data: The full list of players in the database  
- Authentication methods:

### Full list of players in order of most to least goals 
- HTTP request verb: GET
- Required data where applicable: 
- Expected response data: The full list of players in the database from most to least goals   
- Authentication methods:

### Full list of players in order of most to least assists 
- HTTP request verb: GET
- Required data where applicable: 
- Expected response data: The full list of players in the database from most to least assists   
- Authentication methods:

### Full list of players in order of most to least cleansheets 
- HTTP request verb: GET
- Required data where applicable: 
- Expected response data: The full list of players in the database from most to least cleansheets   
- Authentication methods:

### Get the stats of the player you searched
- HTTP request verb: GET
- Required data where applicable: The players name 
- Expected response data: The full stats of the searched player  
- Authentication methods:

### Delete a player 
- HTTP request verb: DELETE
- Required data where applicable: The players name 
- Expected response data: A message confirming the player you deleted 
- Authentication methods: JWT Token and admin role

### Update a player 
- HTTP request verb: PUT/PATCH
- Required data where applicable: The players name 
- Expected response data:
- Authentication methods: JWT Token and admin role

### Adding a new player 
- HTTP request verb: POST
- Required data where applicable: position, team, name, number, goals, assists, cleansheets, form and fitness 
- Expected response data: 
- Authentication methods: JWT Token and admin role



## R6 - An ERD for your app
![ERD](https://user-images.githubusercontent.com/110369771/201511899-8a4b0a67-ec24-4cfc-ae28-e54c69425500.jpg)


## R7 - Detail any third party services that your app will use
At the moment the only third party package that is used in this application is the flask import. This import has allowed my to add authentication and authorisation to this application. It has also been very useful in allowing me to access the datatbase and structuring the application. In the future i would like to impliment a third party application the gives me access to live game statistics to give fans more instight into each game. 


## R8 - Describe your projects models in terms of the relationships they have with each other
### User
- The user model contains id (PK)
- Also contains email or hpone number and password which is used for authorisation
- This models alows has is_admin to confirm the permissions for each user (CRUD Authority)
- The users favourite team is used in this model 
- This also contains the users name 

This model does not have direct relation with other models. The only effect this model has on the others is that it dictates whihc users can  update the players and the table databases.

### Table
- The table model contains the teams position in the table 
- It also contains each teams name (PK) (FK)
- This models contains all of the teams stats for the season as seen above in the ERD 

This models has a realtionship with the players model. Each player has a foreign key linking the team they pkay for with a team in the table model.

### player
- The player model contains each players name (PK)
- It also contains the team they play for (FK)
- The team the player plays for is also in this model (FK)
- This model also contains all of the players stats for the season as seen in the ERD

This model has a relationship with the tbale model. This links each player with the team they play for. In the future i would like to add the feature where for each goal socred by a player this would also reflect a change in the relevent teams goals and goal difference.

## R9 - Discuss the database relations to be implemented in your application
The relationship in this app is the Table model which has a many-to-one relationship with the Players model. This means that the table can have many teams, but a player can only have one team. The Table model has a table.team foreign key which links it to the players model.

## R10 - Describe the way tasks are allocated and tracked in your project
I tracked tasks for my project by making a board in trello. Trello is an Online Management Software System was used to manage the projects development. In trello I created a board that broke down the requirements of each module in the api. 

- Create models 
- Finish the README.md file
- create the main model
- setup and link the database 
- create and link git hub repo

The modular tasks allow for sectioned completion of each module and then are tracked by the progress and debugging of each controllers functions related to the model and/or other task.

Link to trello board 
- https://trello.com/invite/b/8zeso93s/ATTIc1d351b564010451f2ef06bec36ae356819A422F/sonnydavidsont2a2
