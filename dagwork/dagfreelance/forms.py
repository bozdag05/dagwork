from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from dagfreelance.models import ClientModel, ContractorModel


# Форма для регистрации
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User

        fields = ("username", 'email', 'password1', 'password2')


# Форма для авторизации
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User

        fields = ("username", 'password1')


# Форма для редактирования профиля пользователя
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# Форма для редактирования профиля заказчика
class ClientEditForm(forms.ModelForm):
    class Meta:
        model = ClientModel
        fields = ["photo", "date_of_birth", "number", "messages", "description"]


# Форма для редактирования профиля исполнителя
class ContractorEditForm(forms.ModelForm):
    class Meta:
        model = ContractorModel
        fields = ["photo", "date_of_birth", "number", "messages", "experience", "link_resume", "softskills",
                  "hardskills", "specialization", "description"]
