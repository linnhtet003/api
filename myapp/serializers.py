from rest_framework import serializers
from .models import *


class CategoriesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"