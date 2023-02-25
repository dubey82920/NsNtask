from rest_framework import serializers
from NsN.models import Work,Artist

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('link', 'work_type')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'