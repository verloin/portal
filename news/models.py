from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone





class News(models.Model):
    title = models.CharField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    img_author = models.ImageField(default='user.jpg', upload_to='profile_images/')
    body = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('news:detail_news',
                       args=[str(self.id)])

    def __str__(self):
            return self.title