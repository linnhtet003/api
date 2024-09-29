from rest_framework import serializers
from .models import *


class CategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"