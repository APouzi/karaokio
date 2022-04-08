from django.urls import path
from .views import CreateEvent, EventsFavoriteList

# Refresh token for acquiring a new refresh token for registering:
# path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
urlpatterns = [
    # This one is for logging in 
    path('post-event/', CreateEvent.as_view(), name='token_obtain_pair'),
    path('events-list/', EventsFavoriteList.as_view(), name='token_obtain_pair'),
    
]