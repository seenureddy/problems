import random
from datetime import datetime
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from accounts.models import Article, Category


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(posted_on__lte=datetime.today()).order_by('posted_on')
    context_object_name = 'article_list'
    template_name = 'articles/list_articles.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        articles = self.get_queryset()
        article_ids = articles.values_list('id', flat=True)
        try:
            context['random_article'] = articles.get(id=random.choice(article_ids))
        except IndexError:
            return context['article_list']
        return context


class ArticleDetailView(DetailView):
    model = Article
    slug_url_kwarg = 'slug'
    context_object_name = 'article_detail'
    template_name = 'articles/detail_article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(posted_on__lte=datetime.today()).order_by('posted_on')
        return context
