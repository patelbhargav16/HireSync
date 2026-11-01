from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsRecruiter


class JobListCreateView(generics.ListCreateAPIView):
    serializer_class = JobSerializer

    filterset_fields = [
        "job_type",
        "experience_level",
        "location",
        "company_name",
    ]

    search_fields = [
        "title",
        "company_name",
        "location",
        "description",
        "requirements",
        "skills_required",
    ]

    ordering_fields = [
        "created_at",
        "salary_min",
        "salary_max",
        "title",
    ]

    ordering = ["-created_at"]

    def get_queryset(self):
        return Job.objects.filter(is_active=True).order_by("-created_at")

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsRecruiter()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsAuthenticated(), IsRecruiter()]
        return [AllowAny()]

    def get_queryset(self):
        queryset = Job.objects.all()

        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return queryset.filter(recruiter=self.request.user)

        return queryset.filter(is_active=True)