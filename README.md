# SonnyDavidson_T2A2

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
- Required data where applicable: ALL the data required in the "Table" table
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




## R6 - An ERD for your app


## R7 - Detail any third party services that your app will use
This application does not use any third party services. All that is used is flask some other imports to make everything run smoothly.


## R8 - Describe your projects models in terms of the relationships they have with each other
With in this projects I have used then MVC model. this has allowed me to structure my application in a very simple and effcient manner. Each of the models within this 

## R9 - Discuss the database relations to be implemented in your application


## R10 - Describe the way tasks are allocated and tracked in your project

