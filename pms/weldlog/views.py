
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from weldlog.models import Weldlog
from weldlog.serializers import Weldlogserializers
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import viewsets




class WeldlogViewSet(viewsets.ModelViewSet):
    queryset = Weldlog.objects.all()
    serializer_class = Weldlogserializers



