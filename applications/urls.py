
from django.urls import path

from .views import (
    ApplyJobView,
    CandidateApplicationListView,
    RecruiterApplicationListView,
    ApplicationStatusUpdateView,
)

urlpatterns = [
    path("apply/", ApplyJobView.as_view(), name="apply-job"),
    path("my-applications/", CandidateApplicationListView.as_view(), name="my-applications"),
    path("recruiter/", RecruiterApplicationListView.as_view(), name="recruiter-applications"),
    path("<int:pk>/status/", ApplicationStatusUpdateView.as_view(), name="application-status"),
]
