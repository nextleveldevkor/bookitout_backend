from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import loan

list_dook_library = []

@csrf_exempt
@api_view(['GET', 'POST'])
def book_view(request):
  if request.method == 'GET':
    return Response({'method' : 'GET'})
  else:
    keyword = request.data['search_title']
    list_dook_library = loan.search_book_library(keyword)
    return Response(list_dook_library)

@csrf_exempt
@api_view(['GET', 'POST'])
def book_detail_view(request):
  if request.method == 'GET':
    return Response({'method' : 'GET'})
  else:
    keyword = request.data['search_title']
    list_dook_library = loan.search_book_library(keyword)
    return Response(list_dook_library)


# Create your views here.
