from dataclasses import fields
from rest_framework import serializers
from .models import Event
from users.models import EndUserEventsFavoriteList
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventFavoritesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUserEventsFavoriteList
        fields = ['userProfile','events']
        depth = 1