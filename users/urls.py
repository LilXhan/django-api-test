from django.urls import path
from .views import UserView

urlpatterns = [
    path('users/', UserView.as_view(), name='users')
]


# from rest_framework import routers

# router = routers.DefaultRouter()

# router.register('users', UserView, basename='users')

# urlpatterns = router.urls