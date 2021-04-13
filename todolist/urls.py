from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("todolist/", views.todolist, name="todolist"),
]
