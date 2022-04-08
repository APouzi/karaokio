from django.urls import path
from .views import CreateVenue, GetVenueList, GetVenueDetail, VenueFavoriteList

# Refresh token for acquiring a new refresh token for registering:
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
urlpatterns = [
    # This one is for logging in 
    path('post-venue/', CreateVenue.as_view(), name='token_obtain_pair'),
    path('venue-list/', VenueFavoriteList.as_view(), name='token_obtain_pair'),
    path('venue-detail/<str:pk>', GetVenueDetail.as_view(), name='token_obtain_pair'),

]