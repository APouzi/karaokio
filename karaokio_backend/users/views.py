from rest_framework.generics import ListAPIView,  UpdateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView

from .serializers import EndUserWithToken, EndUserUpdateSerializer, EndUserProfilepdateSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import EndUser, UserProfile
# Create user
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .tasks import add

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['adam'] = "leveling up"
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
# these are already included.   
        # data["refresh"] = str(refresh)
        # data["access"] = str(refresh.access_token)

#email, user_name, first_name, last_name, token (includes access and refresh), REMEMBER ".data".
        serializer = EndUserWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterEndUser(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = EndUserWithToken

UserModel = get_user_model()
class UpdateEndUser(UpdateAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = EndUserUpdateSerializer

    def get_object(self):
        return UserModel.objects.get(id = self.request.user.id)

class UserProfileHanlder(RetrieveUpdateAPIView):
    permission_classes = ([IsAuthenticated])
    serializer_class = EndUserProfilepdateSerializer

    def get_object(self):
        add.delay(1,2)
        return UserProfile.objects.get(endUser = self.request.user)
# Handles put AND Patch
    def perform_update(self, serializer):
        serializer.save(endUser = self.request.user)


# Logout user (just delete token from frontend? Not session based)

# Test view
class GetAllUsers(ListAPIView):
    queryset = EndUser.objects.all()
    serializer_class = EndUserWithToken

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