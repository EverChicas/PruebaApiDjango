from rest_framework import serializers
from .models import Credencial

class CredencialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credencial
        fields = ('__all__')