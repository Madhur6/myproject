from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

# Create your views here.
@api_view(['GET'])
def get_data(request):
    # person = {
    #     "name": "Madhur",
    #     "age": 22,
    # }
    # Response object: Render Json data from python-data(dictionary or list) that we pass into it...
    # return Response(person)

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_data(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)