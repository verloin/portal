from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from tasksmanager.forms import ChangeTaskForm, AddCommentForm
from tasksmanager.models import Task, Comment




class TaskListView(ListView):
    queryset = Task.objects.all()
    model = Task
    context_object_name = 'list_tasks'
    template_name = 'taskmanager/list_tasks.html'
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('tasksmanager:list_tasks')
    model = Task
    template_name = 'taskmanager/add_task.html'
    fields = ['status', 'title', 'author', 'executor', 'description']

    users_list = User.objects.all()
    status_list = Task.CHOICES

    # def add_task(request):
    #     users_list = User.objects.all()
    #     status_list = Task.CHOICES
    #
    #     context = {
    #         "users_list": users_list,
    #         "status_list": status_list,
    #     }
    #     return render(request, 'taskmanager/add_task.html', context)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskmanager/detail_task.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = reverse_lazy('tasksmanager:list_tasks')
    model = Task
    template_name = 'taskmanager/edit_task.html'
    form_class = ChangeTaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(task=self.object).order_by('created')
        context['comment_form'] = AddCommentForm(initial={'task': self.object})
        return context


