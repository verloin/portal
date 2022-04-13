
from django.urls import path

from home import views
from home.views import NewsListView, NewsDetailView

urlpatterns = [
    path('home/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('', NewsListView.as_view(), name ='home'),
    path('home/add', views.add_news, name='add_news'),
]
