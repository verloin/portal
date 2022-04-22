from django.urls import path

from tasksmanager.views import TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView



app_name = 'tasksmanager'



urlpatterns = [
	path('', TaskListView.as_view(), name='list_tasks'),
	path('<int:pk>/', TaskDetailView.as_view(), name='detail_task'),
	path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
	path('add/', TaskCreateView.as_view(), name='add_task'),
]