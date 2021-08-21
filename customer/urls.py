from django.urls import path
from customer import views

urlpatterns = [
  path('products/', views.BooksView.as_view()),
]