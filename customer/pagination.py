from rest_framework.pagination import PageNumberPagination
from customer.models import Books


class BooksPagination(PageNumberPagination):
    page_size = 12
