from django.urls import path

from news import views
from news.views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView


app_name = 'news'


urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('<int:pk>/', NewsDetailView.as_view(), name='detail_news'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='edit_news'),
    path('add/', NewsCreateView.as_view(), name='add_news'),
]
