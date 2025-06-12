from django.urls import path
from rest_registration.api.urls import register
from rest_registration.api.views import register, send_reset_password_link, reset_password
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('send-reset-password-link/', send_reset_password_link, name='send-reset-password-link') , 
    path('reset-password/', reset_password , name='reset-password'),
]
