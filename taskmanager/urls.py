from django.urls import path
from taskmanager import views

app_name = 'taskmanager'

urlpatterns = [
    path('index/', views.TaskListView.as_view(), name='index'),
    path('update-task-order/', views.UpdateTaskOrder.as_view(), name='update_task_order'),
]