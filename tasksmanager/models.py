from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
# from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.http import request


from django.contrib.auth.models import User
from django.urls import reverse


class Task(models.Model):

    CHOICES = (
        ('NEW', "Новая"),
        ('QUEUE', "В очереди"),
        ('WORK', "В работе"),
        ('DONE', "Выполнено"),
        ('CANCEL', "Отменённая"),
    )

    title = models.CharField(("Название"), max_length=50)
    description = models.TextField(("Описание"))
    author = models.ForeignKey(User, verbose_name=("Постановщик"), on_delete=models.CASCADE, related_name='tasks')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=("Исполнитель"))
    status = models.CharField(("Статус "), choices=CHOICES, default='NEW', max_length=32)
    created_on = models.DateTimeField(("Дата создания"), auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)

    @property
    def text_status(self):
        choices = dict(self.CHOICES)
        return choices[self.status]

    def get_absolute_url(self):
        return reverse('tasksmanager:list_tasks')


class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(('Комментарий'))
    created = models.DateTimeField(("Дата создания"), auto_now_add=True)