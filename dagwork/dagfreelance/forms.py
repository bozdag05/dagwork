from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from dagfreelance.models import ClientModel, ContractorModel


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ("username", 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

        fields = ("username", 'password1')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ClientEditForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ["photo", "date_of_birth", "number", "messages", "description"]


class ContractorEditForm(forms.ModelForm):
    class Meta:
        model = ContractorModel
        fields = ["photo", "date_of_birth", "number", "messages", "experience", "link_resume", "softskills",
                  "hardskills", "specialization", "description"]
