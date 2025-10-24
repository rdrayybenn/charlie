from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('add-balance/', views.add_balance, name='add_balance'),
    path('users/', views.users_list, name='users'),
    path('rides/', views.rides_list, name='rides'),
]
