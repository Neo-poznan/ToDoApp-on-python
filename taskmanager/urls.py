from django.urls import path
from taskmanager import views

app_name = 'taskmanager'

urlpatterns = [
    path('index/', views.TaskListView.as_view(), name='index'),
    path('update-task-order/', views.UpdateTaskOrder.as_view(), name='update_task_order'),
    path('create-task/', views.AddTaskView.as_view(), name='create'),
    path('delete-task/<int:task_id>/', views.delete_task_view, name='delete'),
    path('create-category/', views.CategoryCreationView.as_view(), name='create_category'),
    path('set-theme/', views.set_theme, name='set_theme')
]