from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from rest_framework.views import APIView

from category_management.models import Category, Subcategory
from category_management.serializer import CategorySerializer
from category_management.inv_json_data import room_id_list, inv_json

import logging


class CategoryList(APIView):
    """
    returns list of categories with its sub-categories
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        data_list = []
        try:
            category_list = Category.objects.all()
            for object in category_list:
                categories = CategorySerializer(object).data
                data_list.append(categories)
            response = {
                "status": status.HTTP_200_OK,
                "message": "Successfully fetched Category List.",
                "data": data_list
            }

        except Category.DoesNotExist as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)

class DeleteCategory(APIView):
    """
    removes of delete specified category
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, cat_id):
        try:
            category = Category.objects.get(id=cat_id)
            deleted, cat = category.delete()
            if deleted:
                response = {
                    "status": status.HTTP_200_OK,
                    "message": "Successfully Deleted {}".format(category.name),
                }

        except Exception as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)


class GetCategory(APIView):
    """
    gets a specified category details
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request, cat_id):
        data = []
        try:
            category = Category.objects.get(id=cat_id)
            cat = CategorySerializer(category).data
            data.append(cat)
            response = {
                "status": status.HTTP_200_OK,
                "message": "Successfully fetched Category.",
                "data": data
            }
        except Exception as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)


class AddCategory(APIView):
    """
    Adds a Category
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            image = request.FILES['image']
            request.data.update({'image': image})

            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
            response = {
                "status": status.HTTP_201_CREATED,
                "message": "Successfully Created Category.",
                "data": serializer.data
            }

        except Exception as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)


"""
    datadict = request.POST.dict()
    image = request.FILES['image']
    subcat_dict ={key.replace('subcat_',''): datadict[key] for key in ['subcat_name','subcat_desc']}
    subcategory = Subcategory.objects.create(**subcat_dict)
    datadict.pop('subcat_name','subcat_desc')
    datadict.update({ 'image': image})
"""


class UpdateCategory(APIView):
    """
    updates a specified category details
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def post(self, request, cat_id):
        try:
            category = Category.objects.get(id=cat_id)
            image = request.FILES['image']
            request.data.update({'image': image})
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
            response = {
                "status": status.HTTP_200_OK,
                "message": "Successfully Updated Category.",
                "data": serializer.data
            }
        except Exception as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)


# ==================================================
#               INV JSON Related
# ==================================================
class FilterInvJson(APIView):
    """
    returns filtered inv_json
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            filtered = []

            for key, sub_dict in inv_json[0].items():
                sub_dict.pop('total_rooms_left')
                key_list = list(sub_dict.keys())
                if list(map(int, key_list)) == room_id_list:
                    print("{} --> {}".format(key, sub_dict))
                else:
                    temp_dict = {}
                    temp_dict[key] = sub_dict
                    filtered.append(temp_dict)

            print(filtered)
            response = {
                "status": status.HTTP_200_OK,
                "message": "Successfully Filtered Inv_json.",
                "data": filtered
            }
        except Exception as exception:
            logging.error("EXCEPTION OCCURED : ", exception)
            response = {
                "status": 404,
                "message": "Something wrong happened!",
                "data": {}
            }
        return Response(response)
