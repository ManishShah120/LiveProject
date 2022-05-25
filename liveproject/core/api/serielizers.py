from rest_framework import serializers
from core.models import CustomUser, Vacation

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
