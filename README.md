# WaterYoPlants

Capstone Project: WaterYoPlants
Bethel, Carlos, Josh, Rudy
5/4/2021

Project Proposal/Abstract:

This project was born from an observation of a growing problem among novice plant owners: many new plant owners don’t know how to properly care for their plants and may forget to water their plants, leading the plants to eventually die. This starts the cycle of buying a plant, forgetting to water the plant, the plant dying, and then buying a new plant all over again. 
Our project hopes to resolve this issue by creating a plant watering reminder, as well as a user-friendly application to get all their plant care information from one source. Though this type of application has already been created, our project differs from the rest. Our team will collect data from the web, which includes a large repository of plant details from the array of types to the type of soil each needs to the amount of water the plants need. Using this web scraped data, we will generate a database to house all of it. Then, we will allow the user to input the type of plant they have, which will correspond to specific plant care information. This will be connected to the email notification system that will be configured to remind the user to water their plant according to the data associated with it. 
Throughout this project, we will be utilizing various packages, but we would like to highlight our use of BeautifulSoup and Urllib to collect our data through the web, as well as Sqllite3 to create our databases and extract data from them, and Tkinter to create our GUI for our application.

Coolest Package!
Tkinter

Tkinter is an open source Python GUI library used as an interface for the Tk GUI toolkit. Tk is an open source software that provides basic elements that build a GUI. For our project, we used Tkinter to specifically create a background image, entry box, labels, a submit button, another window to display output, and incorporated data extraction from the submit button.
Tkinter is very cool because it is an all-in-one GUI toolkit that anyone from a beginner programmer and on could use. It is simple and flexible to any user’s needs. 
Two setbacks we had with Tkinter were connecting the GUI to the database to extract information from the database based on the user’s input and implementing functions to the widgets. By doing plenty of research on Tkinter and how it can interact with databases, we were able to overcome both setbacks. Another setback we faced was trying to stop the output from repeating itself in the new window


Some Other Packages!

SQLite3

SQLite3 provides a SQL interface for the SQLite library. The SQLite library provides a disk-based database eliminates the need for a separate server process an allows you to access it using nonstandard SQL language. We utilized SQLite3 to create a database using web scraped data.
SQLite3 is very user friendly and is an easy way to organize and view a database.
Some setbacks might be knowing to close the connection and cursor, but that is simply a best practice to lighten the load on a computer’s memory. Additionally, one must know how to use the SQL language when creating a database, so we had to do some research when it came to creating tables and how to alter them if need be. 

Requests

Requests is an HTTP library for Python. It allows users to send HTTP requests and eliminates the need for many manual tasks. We used Requests to get all the information for a website.
Requests saves time and energy so that the user can focus on other tasks

Re

Re, also known as regular expressions, allows a user to specify a set of strings and matches it by searching for the specific strings entered. We used regular expressions to comb through the data and search for a certain patterns or strings that matched our needs, so that we could only add the data we needed into our database.
Regular expressions are very cool because, once one learns its language, one can search for any specific pieces of data to find exactly what they are looking for. 
Some setbacks we had were figuring out how to find the specific information in the website when some of the code is inconsistent. 



Contributions

Web Scraping: Carlos

Creating a Database: Bethel

Extracting Data from Database: Rudy

Querying Data: Josh

Notification: Carlos

Creating the GUI: Rudy

Documentation: Bethel

Presentation: Rudy



