from rest_framework import serializers
from .models import chat
 
class chatserializer(serializers.ModelSerializer):
    class Meta:
        model=chat
        fields='__all__'