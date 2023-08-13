from .models import *
from rest_framework import serializers

# Create serializers here

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('__all__')
        
class SingerSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ('__all__')