from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from accounts.slugify import unique_slugify


def upload_image(instance, image):
    """
    Stores the attachment in a "per gallery/module-class/yyyy/mm/dd" folder.
    :param instance, filename
    :returns ex: gallery/Image/2016/03/30/filename
    """
    today = datetime.today()
    return 'gallery/{model}/{year}/{month}/{day}/{image}'.format(
        model=instance._meta.model_name,
        year=today.year, month=today.month,
        day=today.day, image=image,
    )


class Article(TimeStampedModel):
    """
    Article will have the title, body, posted_on date and
    author. From title, body we will know what type of article.
    From author we will who worte the article and which date.

    is_published: True when Article is live. When False it will be visible only
    for the author. Author can view how Article looks like and make approval
    for publishing
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    posted_on = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(
        _("Upload Article Picture"), upload_to=upload_image,
        null=True, blank=True)
    optinal_image = models.ImageField(
        _("Upload Article Picture"), upload_to=upload_image,
        null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        if self.id is None:
            unique_slugify(self, self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])


class Category(models.Model):
    """
    Category: classification of Article in an area of expertise
    Many Category will have one article and one category can have
    many articles.
    """
    name = models.CharField(max_length=50)
    article = models.ForeignKey('Article', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name
