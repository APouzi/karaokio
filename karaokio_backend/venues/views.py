from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Venue
from users.models import EndUserVenueFavoriteList
from .serializers import VenueListSerializer, VenueSerialzier
from rest_framework.permissions import IsAuthenticated
from users.models import EndUserVenueFavoriteList, UserProfile
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS

class VenueUserPermission(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user



# Create your views here.
class GetVenueList(ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerialzier

# we have <str:pk> coming into here and the generics of  handles this
class GetVenueDetail(RetrieveAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerialzier



class CreateVenue(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Venue.objects.all()
    serializer_class = VenueSerialzier
#This is for when we have a foreignkey relating to an account or something and this needs to be created by "request.user" 

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class RetrieveUpdateVenue(RetrieveUpdateAPIView):
    permission_classes = [VenueUserPermission]
    serializer_class = VenueSerialzier

    def get_object(self):
        obj = Venue.objects.get(id = self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    



# Must add logic for missing venues and such, though the only way these would be triggered is if they appear in the frontend in the first place. Still though, for later
class VenueFavoriteList(RetrieveUpdateDestroyAPIView):
    serializer_class = VenueListSerializer
    def get_object(self):
        userProf = UserProfile.objects.get(endUser = self.request.user)
        return EndUserVenueFavoriteList.objects.get(userProfile = userProf)
    # Add to list
    def update(self, request, *args, **kwargs):
        venue = request.data['venue']
        userProf = UserProfile.objects.get(endUser = request.user)
        listToUpdate = EndUserVenueFavoriteList.objects.get(userProfile = userProf)
        listToUpdate.venues.add(venue)
        serializer = VenueListSerializer(listToUpdate)
        return Response(serializer.data)
    # remove from list
    def destroy(self, request, *args, **kwargs):
        venue = request.data['venue']
        userProf = UserProfile.objects.get(endUser = request.user)
        listToUpdate = EndUserVenueFavoriteList.objects.get(userProfile = userProf)
        listToUpdate.venues.remove(venue)
        serializer = VenueListSerializer(listToUpdate)
        return Response(serializer.data)

""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
