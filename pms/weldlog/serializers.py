from dataclasses import field, fields
from rest_framework import serializers
from weldlog.models import Weldlog


class Weldlogserializers(serializers.ModelSerializer):
    class Meta:
        model=Weldlog
        fields = '__all__'



