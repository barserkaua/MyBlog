
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.home, name='home'),
    path('account/create/', views.signUpView, name='signup'),
    path('account/login/', views.loginView, name='login'),
    path('account/logout/', views.logoutView, name='logout'),
]