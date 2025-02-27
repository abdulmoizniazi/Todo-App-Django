from django.urls import path
from . import views


app_name = "todo"

urlpatterns = [
    path("", views.signup, name="index"),
    path("login/", views.user_login, name="login"),
    path("todopage/", views.todo_pg, name= 'todopage'),
    path("signout/", views.signout, name='signout'),
    path("edit_todo/<int:srno>", views.edit_todo, name= 'edit_todo'),
    path("delete_todo/<int:srno>", views.delete_todo, name='delete_todo')
]