from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def book_view(request):
  return HttpResponse('asdasd');

# Create your views here.
