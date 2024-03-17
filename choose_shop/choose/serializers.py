from rest_framework import serializers
from .models import *

class IntroduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intorduce
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class Great_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Great_Product
        fields = '__all__'