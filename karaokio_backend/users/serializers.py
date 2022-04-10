from .models import UserProfile
from rest_framework import serializers
from .models import EndUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

# With this, we only allow the updating of the current fields given to the user who wants to update thier user
class EndUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        fields = ["first_name","last_name"]
    
#     def update(self, instance, validated_data):
# #Super calls the ModelSerializer function of update, while extending it slightly for our needs. 
#         user = super().update(instance, validated_data)
#         user.save()
#         return instance

    
class EndUserProfilepdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["state", "zip", "image"]
    
        
    
EndUserModel = get_user_model()
class EndUserWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = EndUser
        fields = ["email", "user_name", "first_name","last_name","password","token"]
        extra_kwargs = {'password':{'write_only' : True}}##This is how we have the ability to change the password in the serializer BUT not have it sent back in the Response
    
    def create(self, validated_data):
        user = EndUser.objects.create_user(**validated_data)
        return user

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

