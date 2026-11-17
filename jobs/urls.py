
from django.urls import path

from .views import (
    JobListCreateView,
    JobDetailView,
    JobRecommendationView,
)

urlpatterns = [
    path("", JobListCreateView.as_view(), name="job-list-create"),
    path("recommendations/", JobRecommendationView.as_view(), name="job-recommendations"),
    path("<int:pk>/", JobDetailView.as_view(), name="job-detail"),
]
