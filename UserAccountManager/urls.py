from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path
from .views import SignUPView, GoogleOAuth2RedirectView, GoogleOAuth2CallbackView, CustomTokenObtainPairView, UserView, UsersView

urlpatterns = [
    path('signup/', SignUPView.as_view(), name='sign-up'),
    # JWT token endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', UserView.as_view(), name='user-detail'),
    path('all', UsersView.as_view(), name='get-users')
    # social authentication
    # path('oauth/google/redirect/', GoogleOAuth2RedirectView.as_view(), name='google-oauth'),
    # path('oauth/google/callback/', GoogleOAuth2CallbackView.as_view(), name='google-redirect'),
]
