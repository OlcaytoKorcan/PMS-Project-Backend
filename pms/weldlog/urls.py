
from django.urls import re_path as url
from django.urls import path
from weldlog import views
from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'welds', views.WeldlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
