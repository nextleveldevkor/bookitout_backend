from rest_framework import serializers

from customer.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class BooksSerializerGroup(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = Books
        fields = ("title", "author", "count")
