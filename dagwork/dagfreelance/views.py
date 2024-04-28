from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserEditForm, ClientEditForm, ContractorEditForm, UserLoginForm
from .models import ClientModel, ContractorModel
# Create your views here.
from django.views.generic import ListView, DetailView


# Вюха --> Контроллер

# Контроллер главной стр.
def homeview(request):
    return render(request, template_name='dagfreelance/home.html', context={"title": "DagFreelance"})


# Контроллер для авторизации
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'dagfreelance/login.html', {"form": form})


# Контроллер для выхода
def user_logout(request):
    logout(request)
    return redirect('home')


# Контроллер для регистрации заказчика
def register_client(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)

            new_user.set_password(
                form.cleaned_data['password1'])
            new_user.save()
            ClientModel.objects.create(user=new_user)
            login(request, new_user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('client_edit_profile')
        else:
            messages.error(request, 'Произошла какая-то ошибка')
    else:
        form = UserRegisterForm()
    return render(request, 'dagfreelance/register.html', {"form": form})


# Контроллер для редактирования профиля заказчика
@login_required
def edit_client(request):
    if request.method == 'POST':
        form_user = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        form_client = ClientEditForm(instance=request.user.clientmodel, data=request.POST, files=request.FILES)
        if form_user.is_valid() and form_client.is_valid():
            form_user.save()
            form_client.save()
            messages.success(request, 'Изменения успешно сохранены')
            return redirect('home')
        else:
            messages.error(request, 'Произошла какая-то ошибка')
    else:
        form_user = UserEditForm(instance=request.user)
        form_client = ClientEditForm(instance=request.user.clientmodel)

    context = {
        "form_user": form_user,
        "form_client": form_client
    }
    return render(request, 'dagfreelance/client_edit_profile.html', context=context)


# Контроллер для регистрации исполнителя
def register_contractor(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)

            new_user.set_password(
                form.cleaned_data['password1'])
            new_user.save()
            ContractorModel.objects.create(user=new_user)
            login(request, new_user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('contractor_edit_profile')
        else:
            messages.error(request, 'Произошла какая-то ошибка')
    else:
        form = UserRegisterForm()
    return render(request, 'dagfreelance/register.html', {"form": form})


# Контроллер для редактирования профиля исполнителя
@login_required
def edit_contractor(request):
    if request.method == 'POST':
        form_user = UserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        form_contractor = ContractorEditForm(instance=request.user.contractormodel, data=request.POST,
                                             files=request.FILES)
        if form_user.is_valid() and form_contractor.is_valid():
            form_user.save()
            form_contractor.save()
            messages.success(request, 'Изменения успешно сохранены')
            return redirect('home')
        else:
            messages.error(request, 'Произошла какая-то ошибка')
    else:
        form_user = UserEditForm(instance=request.user)
        form_contractor = ContractorEditForm(instance=request.user.contractormodel)

    context = {
        "form_user": form_user,
        "form_contractor": form_contractor
    }
    return render(request, 'dagfreelance/contractor_edit_profile.html', context=context)


# Контроллер для представления списка заказчиков
class ClientListView(ListView):
    model = ClientModel
    template_name = 'dagfreelance/client.html'
    context_object_name = 'clients'


# Контроллер для представления списка исполнителй
class ContractorListView(ListView):
    model = ContractorModel
    template_name = 'dagfreelance/contractor.html'
    context_object_name = 'contractors'


# Контроллер для получения определённой записи заказчика
class ProfileClient(DetailView):
    model = ClientModel
    template_name = 'dagfreelance/profile_client.html'
    context_object_name = 'client'


# Контроллер для получения определённой записи исполнителя
class ProfileContractor(DetailView):
    model = ContractorModel
    template_name = 'dagfreelance/profile_contractor.html'
    context_object_name = 'contractor'
