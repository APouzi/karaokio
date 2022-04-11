from dataclasses import fields
from rest_framework import serializers
from .models import Venue
from users.models import EndUserVenueFavoriteList

class VenueSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id','name','description', 'state', 'zip', 'has_nft', 'created_by', 'image']
    
class VenueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUserVenueFavoriteList
        fields = ['userProfile','venues']
        depth = 1
        