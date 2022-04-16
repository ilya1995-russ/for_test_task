from statistics import mode
from django import forms
from django.forms import fields, widgets
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AuthorUser
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = AuthorUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()

        return user
