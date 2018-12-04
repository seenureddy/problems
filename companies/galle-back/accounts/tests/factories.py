import datetime
import pytz
from django.conf import settings

# Third Party Stuff
import factory
from factory import fuzzy


from accounts.models import Article, Category


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    email = factory.Sequence(lambda n: 'user%04d@example.com' % n)
    first_name = factory.Sequence(lambda n: 'First Name{}'.format(n))
    last_name = factory.Sequence(lambda n: 'Last Name{}'.format(n))
    password = factory.PostGeneration(
        lambda obj, *args, **kwargs: obj.set_password('123123'))


def create_user(**kwargs):
    "Create an user along with their dependencies"
    return UserFactory.create(**kwargs)


class ArticleFactory(factory.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: 'Article title{}'.format(n))
    body = factory.Sequence(lambda n: 'Article body{}'.format(n))
    posted_on = fuzzy.FuzzyDateTime(
        datetime.datetime(2016, 6, 7, tzinfo=pytz.UTC))
    image = factory.django.ImageField(color='blue')


    class Meta:
        model = Article


class CategoryFactory(factory.DjangoModelFactory):
    name = "Category Name"
    article = factory.SubFactory(ArticleFactory)

    class Meta:
        model = Category
