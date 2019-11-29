from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django.db import connection,connections



# Create your views here.
@api_view(["POST"])
def IdealWeight(heightdata):
    try:
        height=json.loads(heightdata.body)
        weight=str(height*10)
        return JsonResponse("Ideal Weight should be:"+weight+" Kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
#def GetData(self):
#    cursor = connection.cursor()
#    #number_of_rows=cursor.execute("Select * from transportdtl;")
#    cursor.execute("Select TransNo,LogiCode,LogiName from transportdtl LIMIT 5;")
#    data = cursor.fetchall()
#    return JsonResponse(data,safe=False)
def GetData(self):
    #cursor = connection.cursor()
    connection=connections["My12"]
    cursor = connection.cursor()
    # cursor.execute("SELECT userid,username,CAST(isactive as decimal) isactive,createdby,createduser,createddate FROM Demodb.mst_user;")
    cursor.execute("CALL GetUser(1);")
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
         json_data.append(dict(zip(row_headers,result)))
    return JsonResponse(json_data,safe=False)