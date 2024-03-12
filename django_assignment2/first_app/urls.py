from django.urls import path
from . import views

urlpatterns = [
    path('add_task', views.home, name='addtask'),
    path('', views.show_tasks, name='showtasks'),
    path('edit_task/<str:Title>', views.edit_task, name='edit_task'),
    path('delete_task/<str:Title>', views.delete_task, name='delete_task'),
]
