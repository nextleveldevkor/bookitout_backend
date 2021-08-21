from django.db.models.lookups import PostgresOperatorLookup
from django_filters import rest_framework as filters
from customer.models import Books
from django.db.models import Q

class BooksFilter(filters.FilterSet):
  title = filters.CharFilter(
    field_name='title',
    label='title'
  )
  class Meta:
    model = Books
    fields = {
      'title': [
        'contains'
      ],
    }