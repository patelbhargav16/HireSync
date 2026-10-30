
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CandidateRegistrationView,
    RecruiterRegistrationView,
    CustomTokenObtainPairView,
    CandidateDashboardView,
    RecruiterDashboardView,
)

urlpatterns = [
    # Registration
    path("register/candidate/", CandidateRegistrationView.as_view()),
    path("register/recruiter/", RecruiterRegistrationView.as_view()),

    # Authentication
    path("login/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),

    # Role-based dashboards
    path("candidate/dashboard/", CandidateDashboardView.as_view()),
    path("recruiter/dashboard/", RecruiterDashboardView.as_view()),
]
