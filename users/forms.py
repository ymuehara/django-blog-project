from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# first form that inherits from the user creation form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # default equal to True

    class Meta:  # gives a nested name space for configurations. And keeps the configurations in one place.
        model = User  # when form validates it's gonna create a new user
        # fields that will be shown in our form. password2 is the confirmation
        fields = ['username', 'email', 'password1', 'password2']
