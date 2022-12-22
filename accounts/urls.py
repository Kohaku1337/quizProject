from django.urls import path
from rest_framework.routers import DefaultRouter
from accounts.views import *

urlpatterns = [
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile")
]
