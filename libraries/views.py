from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import loan

@csrf_exempt
def book_view(request):
  if request.method == 'GET':
    res = loan.search_book_library('Engineering')
    return JsonResponse(res[0])
  else:
    return JsonResponse({'method' : 'POST'})

# Create your views here.
