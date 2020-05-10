from django import forms
from django.contrib.auth.forms import UserCreationForm
from reminder.models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.RegexField(regex="[0-9]{3}-[0-9]{3}-[0-9]{4}", help_text = "Phone number must be in 123-456-7890 format")
    class Meta:
	    model = CustomUser
	    fields = ["username", "email", "phone", "password1", "password2"]