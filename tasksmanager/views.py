from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView, DetailView


# Create your views here.
from tasksmanager.forms import ChangeTaskForm, AddCommentForm
from tasksmanager.models import Task, Comment



class TaskListView(ListView):
    # login_url = reverse_lazy('login')
    queryset = Task.objects.all()
    model = Task
    template_name = 'taskmanager/_base_task.html'
    paginate_by = 10


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'taskmanager/add_task.html'
    fields = ['status', 'title', 'author', 'executor', 'description']


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskmanager/detail_task.html'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    # login_url = reverse_lazy('login')
    model = Task
    template_name = 'taskmanager/edit_task.html'
    form_class = ChangeTaskForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(task=self.object).order_by('created')
        context['comment_form'] = AddCommentForm(initial={'task': self.object})
        return context