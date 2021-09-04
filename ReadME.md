Group Project - Average Joe's


I was asked to produce a Gym Web Application that could do the following things as MVP.

MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class

My Approach to the Project was to make each file as single focussed as possible and this is why i split the files into the following folders:
-Models - This stored the Objects i was creating and would reuse to how the data i.e (members, Activities and Bookings)

-DB  - This stored the information and start up file for the database as well as the run_sql function for accessing the database.

-Repositories  - This stores all the functions used to retrieve or update and input the information in the database using the run_sql function

-Controllers  - This folder stored all my RESTFUL routes used to connect the HTML templates and the data from the DB so it can be stored in the appropriate URL.

-Templates & Static  - These folders stored all the HTML and CSS word that was then showing the relevant information to the Client.

Using the Flask run command when in the terminal and in the appropriate folder you will be able to start he application and navigate through the web pages.
