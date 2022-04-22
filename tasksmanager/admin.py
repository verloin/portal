from django.contrib import admin

# Register your models here.
from tasksmanager.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'author', 'executor', 'created_on')
    ordering = ('-created_on', )


