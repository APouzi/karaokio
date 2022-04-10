from django.urls import path
from .views import CreateVenue, GetVenueList, RetrieveUpdateVenue, VenueFavoriteList

# Refresh token for acquiring a new refresh token for registering:
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
urlpatterns = [
    # This one is for logging in 
    path('venues', GetVenueList.as_view(), name ='get-venues'),
    path('post-venue/', CreateVenue.as_view(), name='post-venues'),
    path('venue-list/', VenueFavoriteList.as_view(), name='token_obtain_pair'),
    path('venue-detail/<str:pk>', RetrieveUpdateVenue.as_view(), name='token_obtain_pair'),
]