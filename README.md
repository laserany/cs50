# Project Final

Reminder Application

## Backend:

admin.py : added the models to easily view them in the admin site. Also Added a custom user model with a custom user admin.

forms.py : overrided the UserCreationForm to include additional fields like the email and phone number.

models.py : 4 models which are Custom User (has additional phone number field), Group (allows to send reminder to a group of people), Record(records each reminder), GroupMember(member of a specific group).

urls.py : main page along with register and login default pages from django.contrib.auth.urls

views.py : includes the following functions
  index(request): hosts the main page that allows to send a reminder to a single user or a group of people
  register(request): registering new users
settings.py : added additional constants to set out the login and logout redirect URLS. Also the SMTP settings to send confirmation emails using gmail SMTP server. Also added a customized Auth User Model and installed phone_field app.

## Frontend:

login.html and register.html : used to login and register the user. I've used the default django way to create these html files

index.html : the main page that allows you to create a group, add a member to that group, and a form that allows you to send a reminder using email, text or call to yourself or to a group
