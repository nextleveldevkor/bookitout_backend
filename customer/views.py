from django.db.models.query import QuerySet
from rest_framework import decorators, mixins, serializers
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count
from customer.models import Books
from customer.serializer import BooksSerializer, BooksSerializerGroup
from customer.filter import BooksFilter

class BooksViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
  queryset = Books.objects.all().order_by('-id')
  serializer_class = BooksSerializer

class BooksSearchViewSet(GenericViewSet, mixins.ListModelMixin):
  queryset = Books.objects.values('title').annotate(count=Count('title'))
  print(queryset)
  serializer_class = BooksSerializerGroup
  filterset_class = BooksFilter

# newQuery = Books.objects.values('title').annotate(dcount=Count('title'))
#     print(newQuery)
# Create your views here.
