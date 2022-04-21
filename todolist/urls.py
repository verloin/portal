from django.urls import re_path

from todolist.views import todo, category


app_name = 'todolist'


urlpatterns = [
	re_path(r'^todo/', todo, name="TodoList"),
	re_path(r'^category/', category, name="Category"),
]