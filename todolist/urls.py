from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_todolist, name='add_todolist'),
    path('delete/<int:id>', delete, name='delete'),
    path('toggle/<int:id>', toggle_completion, name='toggle_completion'),
    path('json/', get_json, name="get_json"),
    path('add/', add_todolist_ajax, name="add_todolist_ajax" )
]
