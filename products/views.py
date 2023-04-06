from django.shortcuts import render

from . serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from uritemplate import partial
from sqlalchemy import create_engine
import psycopg2 
import pandas as pd
from glob import glob
import io
import shutil
import os
from productadmin.settings import BASE_DIR
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets, permissions


# Create your views here.
@api_view(['GET'])
def ProductView(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ProductDetail(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def ProductUpdate(request, pk):
    #permission_classes = [IsAuthenticated]
    product = Product.objects.get(id=pk)
    if request.method == 'PUT':

        serializer = ProductSerializer(instance=product, data=request.data, many = False, partial=True)

    if serializer.is_valid():
        serializer.save()
    else:
         print("something went wrong")
    return Response(serializer.data)


@api_view(['POST'])
def ProductCreate(request):
        if request.method == "POST":

            serializer = ProductSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()
        else:
             print("something wrong")

        return Response(serializer.data)



@api_view(['GET'])
def Product_Import(request):
     csv = glob('media/files/*.csv')[0]
     csv_data = pd.read_csv( csv)

     for record in csv_data.to_dict(orient="records"):
            
                Product.objects.create(
                    name = record['name'],
                    category_id = record['category_id'],
                    unit_price = record['unit_price'],
                    tags = record['tags'],
                    purchase_price = record['purchase_price'],
                    current_stock = record['current_stock']
                )
            
     
     return Response("Products listed successfully") 


@api_view(['GET'])
def ProductClean(request):
     lastSeenId = float('-Inf')
     rows = Product.objects.all().order_by('id')

     for row in rows:
          if row.id == lastSeenId:
               row.delete() # We've seen this id in a previous row
          else: # New id found, save it and check future rows for duplicates.
               lastSeenId = row.id
     return Response("Duplicates eliminated successfully")


class ProductFileViewSet(viewsets.ModelViewSet):
     queryset = File.objects.all()
     serializer_class = FileSerializer
     permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def DeleteProductFile(request):
          # This is your folder path
     file_location = os.path.join(BASE_DIR, 'media/files')

     # Here, lets delete the file
     shutil.rmtree(file_location, ignore_errors = True)
     # making ignore_errors = True will not raise a FileNotFoundError
     return Response("file deleted successfully!")
