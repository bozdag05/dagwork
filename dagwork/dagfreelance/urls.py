from django.urls import path
from .views import homeview, ClientListView, ContractorListView, register_client, edit_client, register_contractor, \
    edit_contractor, user_login, user_logout, ProfileClient, ProfileContractor

urlpatterns =[
    path('', homeview, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('clientlist/', ClientListView.as_view(), name='client_list'),
    path('contractorlist/', ContractorListView.as_view(), name='contractor_list'),
    path('register_client/', register_client, name='register_client'),
    path('register_contractor/', register_contractor, name='register_contractor'),
    path('edit_client/', edit_client, name='client_edit_profile'),
    path('edit_contractor/', edit_contractor, name='contractor_edit_profile'),
    path('profile_client/<int:pk>', ProfileClient.as_view(), name='profile_client'),
    path('profile_contractor/<int:pk>', ProfileContractor.as_view(), name='profile_contractor'),

]