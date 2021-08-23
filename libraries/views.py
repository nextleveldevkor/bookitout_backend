from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import loan

list_book_library = []


@csrf_exempt
@api_view(["GET", "POST"])
def book_view(request):

    if request.method == "GET":
        return Response({"method": "GET"})
    else:
        keyword = request.data["search_title"]
        list_book_library = loan.search_book_library(keyword)
        if not list_book_library:
            return Response({"Error": "No search results"})
        return Response(list_book_library)


@csrf_exempt
@api_view(["GET", "POST"])
def book_detail_view(request):
    if request.method == "GET":
        return Response({"method": "GET"})
    else:
        status_book_library = loan.status_book_library(request.data["link"])
        return Response(status_book_library)


# Create your views here.
