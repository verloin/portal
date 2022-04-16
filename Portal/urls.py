from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('news.urls')), # нужно сменить на домашнюю страницу

]
