from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.tests import factories


class UserModelTestCase(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        u = self.User.objects.create_user(
            username='test@example.com', password='abc')
        assert u.is_active is True
        assert u.is_staff is False
        assert u.is_superuser is False
        assert u.username == 'test@example.com'
        assert str(u) == 'test@example.com'

    def test_create_super_user(self):
        user = self.User.objects.create_user(
            username='test@example.com', password='abc')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        assert user.is_active is True
        assert user.is_staff is True
        assert user.is_superuser is True


class ArticleTestCase(TestCase):

    def test_create_article(self):
        article = factories.ArticleFactory.create()
        assert article.author is not None


class CategoryTestCase(TestCase):

    def test_create_article(self):
        category = factories.CategoryFactory.create()
        assert category.article is not None
