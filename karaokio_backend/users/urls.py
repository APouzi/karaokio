from django.urls import path
from .views import RegisterEndUser, MyTokenObtainPairView, UserProfileHanlder, GetAllUsers, UpdateEndUser
from venues.views import RetrieveUpdateVenue
from rest_framework_simplejwt.views import TokenObtainPairView
# Refresh token for acquiring a new refresh token for registering:
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
urlpatterns = [
    # This one is for logging in 
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterEndUser.as_view(), name = "register_the_new_user"),
    path('profile/', UserProfileHanlder.as_view(), name = "register_the_new_user"),
    path('updateAuth/', UpdateEndUser.as_view(), name = "end-user-update"),
    path('all/', GetAllUsers.as_view(), name = "test"),
    path('RetrieveUpdateVenue/',  RetrieveUpdateVenue.as_view(), name = "Updating-favorite-list"),

]