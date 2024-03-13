from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import *
from rest_framework import generics, viewsets
from .models import * 
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


#==============================================Function Based Views ==========================================================

#3 Function based views 

#3.1 GET POST
@api_view(['GET', 'POST'])
def info_Products(request):
    # GET
    if request.method == 'GET':
        products = Products_serializers.objects.all()
        serializer = Info_Product__serializers(products, many=True)  

        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = Info_Product__serializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


#3.1 GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def info_Product(request, id):
    try:
        product = Products_serializers.objects.get(id=id)
    except Products_serializers.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = Info_Product__serializers(product)
        return Response(serializer.data)
        
    # PUT
    elif request.method == 'PUT':
        serializer = Info_Product__serializers(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


#==============================================GENERICS==========================================================


# 2 Generics 
#2.1 get and post
class generics_list(generics.ListCreateAPIView):
    queryset = Products_serializers.objects.all()
    serializer_class = Info_Product__serializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#2.2 get put and delete 
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products_serializers.objects.all()
    serializer_class = Info_Product__serializers


#==============================================GENERICS==========================================================

#7 viewsets
class viewsets_product(viewsets.ModelViewSet):
    queryset = Products_serializers.objects.all()
    serializer_class = Info_Product__serializers


