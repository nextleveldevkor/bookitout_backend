from rest_framework import decorators, mixins, serializers
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from django.db.models import Count

from customer import serializer
from customer.serializer import BooksSerializer, BooksSerializerGroup, Books

class BooksView(APIView):
  queryset = Books.objects.all().order_by('-id')
  serializer_class = BooksSerializer
  
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)

  def get(self, request):
    serializer = self.serializer_class(self.queryset.all(), many=True)
    return Response(serializer.data)



# newQuery = Books.objects.values('title').annotate(dcount=Count('title'))
#     print(newQuery)
# Create your views here.
