import random
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import mixins
from rest_framework import viewsets

from accounts.models import Article
from accounts.filters import SearchFilterBackend
from accounts.serializers import UserSerializer, ArticleSerializer, SearchSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-posted_on')
    serializer_class = ArticleSerializer


class SearchViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all().order_by('-posted_on')
    serializer_class = SearchSerializer
    filter_backends = (SearchFilterBackend, )
