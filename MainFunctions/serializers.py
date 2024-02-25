from rest_framework import serializers
from .models import Personas

class SerializerPersonas(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ('id', 'Nombres', 'Apellidos', 'Edad')

