from django.contrib.auth.models import User
from rest_framework import filters


class SearchFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        username = request.query_params.get('username', None)
        email = request.query_params.get('email', None)
        title = request.query_params.get('title', None)

        if title:
            return queryset.filter(title__search=title)
        elif email:
            print queryset.filter(author__in=User.objects.filter(email=email).values_list('id', flat=True))
            return queryset.filter(author__in=User.objects.filter(email=email).values_list('id', flat=True))
        elif username:
            return queryset.filter(author__username=username)

