# Project 3

Web Programming with Python and JavaScript

## Backend:

admin.py : added the models to the admin site so that administrators can add/delete/update the orders

forms.py : overrided the UserCreationForm to include additional fields like the email.

models.py : includes 1 model for order plus 2 extra models for regular and sicilian toppings. Overrided the save method to auto calculate the price of the orders based on other attributes of the order. Also added additional boolean field to each of them called placed. If it is False it means that the order was not placed otherwise True.

urls.py : created url patterns for main page, placing order and viewing orders (for admin staff). Used django.contrib.auth.urls pattern for automated login and logout url paths.

views.py : includes the following functions
  index(request): hosts the main page if it is a get request or add order to cart if it is a post request
  cart(request): a page where users can view their virtual cart and then place their orders
  register(request): registering new users
  place_order(request): used to place orders by setting the placed field from False to True. Also sends a confirmation email (The personal touch)
  view_orders(request): for staff members only. Allows them to view the orders that were placed
settings.py : added additional constants to set out the login and logout redirect URLS. Also the SMTP settings to send confirmation emails using sendgrid SMTP server

## Frontend:

login.html and register.html : used to login and register the user. I've used the default django way to create these html files

cart.html : uses for loop to loop through the items that are in the user carts with a button to place an order

index.html : the main page which has a logic to add dropdown lists based on the order that the user picked. has a (add to cart), (view cart) and (logout) buttons

view_orders.html : for staff members to view all the orders that have been placed


  



