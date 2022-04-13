from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView

from home.forms import NewsForm
from home.models import News


class NewsListView(ListView):
    queryset = News.objects.all()
    context_object_name = 'news'
    paginate_by = 3
    template_name = 'home/home.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'home/news_detail.html'


def news_list(request):
    object_list = News.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request,
                  'home/home.html', {
                      'page': page,
                      'news': news
                  })


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.publish = timezone.now()
            news.save()

            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request,
                  'home/add_news.html', {
                      'form': form
                  })