from rest_framework import decorators, mixins, serializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from django.db.models import Count

from customer.serializer import BooksSerializer, BooksSerializerGroup, Books

class BooksViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
  queryset = Books.objects.all().order_by('-id')
  serializer_class = BooksSerializer





# newQuery = Books.objects.values('title').annotate(dcount=Count('title'))
#     print(newQuery)
# Create your views here.
