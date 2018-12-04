from rest_framework import routers

from accounts import viewsets

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'search', viewsets.SearchViewSet, base_name="search")
router.register(r'articles', viewsets.ArticleViewSet)
