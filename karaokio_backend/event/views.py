from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import EventSerializer, EventFavoritesListSerializer
from .models import Event
from users.models import EndUserEventsFavoriteList, UserProfile
from rest_framework.response import Response
# Create your views here.

class CreateEvent(CreateAPIView):
    serializer_class = EventSerializer
    query_set = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class EventList(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class CreatedByUser(RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        events = Event.objects.get(created_by = self.request.user)
        return events


#TODO change to APIVIEW
#Was going to add validation but validation comes from front since it wouldn't be possible to have 
class EventsFavoriteList(APIView):
    def get(self, request, format=None):
        userProf = UserProfile.objects.get(endUser = request.user)
        result = EndUserEventsFavoriteList.objects.get(userProfile = userProf)
        serializer_class = EventFavoritesListSerializer(result)
        return Response(serializer_class.data)
    # Add to list
    def patch(self, request, format=None):
        events = request.data['event']
        userProf = UserProfile.objects.get(endUser = request.user)
        listToUpdate = EndUserEventsFavoriteList.objects.get(userProfile = userProf)
        listToUpdate.events.add(events)
        serializer = EventFavoritesListSerializer(listToUpdate)
        return Response(serializer.data)
    # remove from list
    def delete(self, request, format=None):
        events = request.data['event']
        userProf = UserProfile.objects.get(endUser = request.user)
        listToUpdate = EndUserEventsFavoriteList.objects.get(userProfile = userProf)
        listToUpdate.events.remove(events)
        serializer = EventFavoritesListSerializer(listToUpdate)
        return Response(serializer.data)
    
