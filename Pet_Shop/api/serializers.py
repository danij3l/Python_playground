from rest_framework import serializers
from Home.models import Animals

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Animals
        fields = '__all__'
