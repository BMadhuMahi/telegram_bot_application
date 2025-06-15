from django.urls import path
from .views import public_view, protected_view, register_user,telegram_webhook
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('public/', public_view),
    path('bot/', telegram_webhook),
    path('protected/', protected_view),
    path('register/', register_user),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]
