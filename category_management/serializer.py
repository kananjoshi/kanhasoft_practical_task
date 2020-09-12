from rest_framework import serializers
from category_management.models import Category, Subcategory

class SubcategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Subcategory
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(read_only=True,many=True)
    class Meta:
        model = Category
        fields = "__all__"






