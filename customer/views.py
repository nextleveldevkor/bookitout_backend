from django.db.models.query import QuerySet
from rest_framework import decorators, mixins, pagination, serializers
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.db.models import Count
from customer.models import Books
from customer.serializer import BooksSerializer, BooksSerializerGroup
from customer.filter import BooksFilter
from customer.pagination import BooksPagination


class BooksViewSet(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Books.objects.all().order_by("-id")
    serializer_class = BooksSerializer
    pagination_class = BooksPagination


class BooksSearchViewSet(GenericViewSet, mixins.ListModelMixin):

    queryset = Books.objects.values("title", "author").annotate(count=Count("title"))

    def get_queryset(self, group=True):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method." % self.__class__.__name__
        )
        if group:
            queryset = self.queryset
        else:
            queryset = Books.objects.all().order_by("price")
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    serializer_class = BooksSerializerGroup
    filterset_class = BooksFilter

    @decorators.action(methods=["GET"], detail=False)
    def details(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(group=False))

        serializer = BooksSerializer(queryset, many=True)
        return Response(serializer.data)


# Create your views here.
