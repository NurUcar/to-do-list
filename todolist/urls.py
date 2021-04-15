from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.todolist, name="todolist"),
    path("login/", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("todolist/", views.todolist, name="todolist"),
    path("todolist/addList", views.addtodo, name="addtodo"),
    path("todolist/deleteList/<int:id>", views.deleteToDo, name="deleteToDo"),
    path("todolist/deleteItem/<int:id>", views.deleteItem, name="deleteItem"),
    path("todolist/additem", views.addItem, name="addItem"),
    path("todolist/search", views.searchItem, name="searchItem"),
    path("todolist/filter", views.filterItem, name="filterItem"),
    path("todolist/order", views.orderItem, name="orderItem"),
]
