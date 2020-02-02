# Project 2

Web Programming with Python and JavaScript

This project includes 2 files, index.html which represents frontend/client and application.py which represents the server

index.html : It uses handlebars templating engine. Includes the personal touch which changes the document title when a new message is received in the first line using the onmouseover event. It has 2 templates. One that is before the user chooses his display name and one that is after he chooses his display name. It stores most of the information in the localStorage. The main javascript functions include the following :-

index(): This is the main function that gets invoked in all clickable events. It basically updates the localStorage and re-render the page.

createDisplayName() : creates the display name and saves it in the localStorage.

createChannel() : creates the channel if it didn't exist in the server otherwise will show an error message to the user.

chooseChannel() : updates the channel chosen by the user.

createMessage() : creates a new message in the selected channel and saves it in the server by emitting it through the socket (create_message).

application.py : includes 2 routes and one socket which are :-

("/") : this is to render index.html to the main page.
("/channel", method = 'POST') : updates the channels dictionary by appending a new channel.
("create_message") socket : updates the channels dictionary when a new message is created from the client side (but makes sure that it only updates the most 100 recent ones) and then emits the results back to the ("messages") socket.
