from django.urls import re_path, path
from taskmanager.views import index



app_name = 'taskmanager'


urlpatterns = [
	path('', index, name='tasks'),

]