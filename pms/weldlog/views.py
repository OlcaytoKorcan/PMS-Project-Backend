
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from weldlog.models import Weldlog
from weldlog.serializers import Weldlogserializers

@csrf_exempt
def Weldlogapi(request,id=0):
    if request.method=='GET':
        welds=Weldlog.objects.all()
        weldlog_serializers=Weldlogserializers(welds,many=True)
        return JsonResponse(weldlog_serializers.data,safe=False)