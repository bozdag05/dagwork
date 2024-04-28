from django.urls import path
# Импортируем наши вюхи
from .views import homeview, ClientListView, ContractorListView, register_client, edit_client, register_contractor, \
    edit_contractor, user_login, user_logout, ProfileClient, ProfileContractor

urlpatterns =[
    path('', homeview, name='home'), # Ссылка на главную страницу
    path('login/', user_login, name='login'), # Ссылка для авторизации
    path('logout/', user_logout, name='logout'), # Ссылка выхода
    path('clientlist/', ClientListView.as_view(), name='client_list'), # Ссылка на стр. с зазазчиками
    path('contractorlist/', ContractorListView.as_view(), name='contractor_list'), # Ссылка на стр. с исполнителями
    path('register_client/', register_client, name='register_client'), # Ссылка для регистрации как заказчиками
    path('register_contractor/', register_contractor, name='register_contractor'), # Ссылка для рег. как исполнитель
    path('edit_client/', edit_client, name='client_edit_profile'), # Ссылка для редактирования профиля; заказчик
    path('edit_contractor/', edit_contractor, name='contractor_edit_profile'), # Ссылка для редакт. профиля; исполнитель
    path('profile_client/<int:pk>', ProfileClient.as_view(), name='profile_client'), # Получение определённой записи заказчика
    path('profile_contractor/<int:pk>', ProfileContractor.as_view(), name='profile_contractor'), # Получение опр. записи исполнителя

]