from django.urls import path
from libraries import views

urlpatterns = [
    path("", views.book_view),
    path("status/", views.book_detail_view),
]
