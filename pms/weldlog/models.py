from pickle import TRUE
from pyexpat import model
from random import choices
from secrets import choice
from unittest import result
from django.db import models

# Create your models here.
Y='Y'
N='N'
Accept='Accept'
Reject='Reject'
yn=[
    (Y,'Y'),
    (N,'N')
]
results=[
    (Accept,'Accept'),
    (Reject,'Reject')
]

class Weldlog(models.Model):
    line=models.CharField(max_length=100,blank=False)
    isometry=models.CharField(max_length=100,blank=False)
    spool=models.CharField(max_length=100,blank=False)
    joint=models.CharField(max_length=100,blank=False)
    dia=models.PositiveSmallIntegerField(blank=False)
    mat1=models.CharField(max_length=100,blank=False)
    p1=models.PositiveSmallIntegerField(blank=False)
    mat2=models.CharField(max_length=100,blank=False)
    p2=models.PositiveSmallIntegerField(blank=False)
    fitupdate=models.DateField(null=True, blank=True)
    fitupresult=models.CharField(max_length=20,blank=True)
    weldclass=models.CharField(max_length=10,blank=False)
    pwht=models.CharField(max_length=100,blank=False,choices=yn)
    wps=models.CharField(max_length=10,blank=True)
    location=models.CharField(max_length=10,blank=False)
    weldtype=models.CharField(max_length=100,blank=False)
    welder=models.CharField(max_length=100,blank=True)
    vtdate=models.DateField(null=True, blank=True)
    vtreport=models.CharField(max_length=100,blank=True)
    pwhtdate=models.DateField(null=True, blank=True)
    pwhtreport=models.CharField(max_length=100,blank=True)
    rtdate=models.DateField(null=True, blank=True)
    rtreportno=models.CharField(max_length=100,blank=True)
    rtresult=models.CharField(max_length=100,blank=True,choices=results)
    rtrate=models.PositiveSmallIntegerField(null=True, blank=True)
    pwhtrate=models.PositiveSmallIntegerField(null=True, blank=True)
    penalty=models.CharField(max_length=100,blank=True)
    tpno=models.CharField(max_length=100,blank=True)
    cancel=models.CharField(max_length=100,blank=True)
