from dataclasses import field, fields
from rest_framework import serializers
from weldlog.models import Weldlog


class Weldlogserializers(serializers.ModelSerializer):
    weld=serializers.IntegerField()
    class Meta:
        model=Weldlog
        fields = ('line', 'weld','rtrate')



