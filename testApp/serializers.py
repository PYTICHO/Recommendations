from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author')  # "__all__"


class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tovar
        fields = "__all__"
