
from django.urls import re_path as url
from django.urls import path
from app_weldlog import views


urlpatterns = [
    # path('as/', views.Weldlogapi),
    path('weldlogs/', views.getWeldlogs),

]
