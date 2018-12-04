from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import ArticleListView, ArticleDetailView


urlpatterns = [
    url(r'^articles/$', ArticleListView.as_view(), name='article-list'),
    url(r'^detail/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
