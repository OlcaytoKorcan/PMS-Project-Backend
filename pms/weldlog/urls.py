
from django.urls import re_path as url
from django.urls import path
from weldlog import views




urlpatterns = [
    path('as/',views.Weldlogapi),

]
