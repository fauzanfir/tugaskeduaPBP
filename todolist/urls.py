from django.urls import path
from todolist.views import create_task, delete_task, register, show_task, update_task
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import post_ajax_todolist, show_json, show_json_by_id, show_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_task, name='show_task'),  
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('add/', create_task, name='create_task'),
    path('update-task/<int:id>', update_task, name='update_task'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('ajax/submit', post_ajax_todolist, name="post_ajax_todolist")
]