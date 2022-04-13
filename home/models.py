from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone





class News(models.Model):
    title = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
            return self.title





