from .models import Personas
from .serializers import SerializerPersonas
from rest_framework import viewsets, permissions


class PersonasViewsets(viewsets.ModelViewSet):
    queryset= Personas.objects.all()
    serializer_class= SerializerPersonas
    permission_classes= [permissions.AllowAny]

    