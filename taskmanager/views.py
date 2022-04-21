from django.shortcuts import render

# Create your views here.





def index(request):
    return render(request, 'taskmanager/_base_task.html') #  вывод страницы с задачами