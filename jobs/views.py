
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job
from .serializers import JobSerializer
from .services import calculate_job_match

from resumes.models import Resume
from accounts.permissions import IsRecruiter, IsCandidate


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


class JobRecommendationView(APIView):
    permission_classes = [IsAuthenticated, IsCandidate]

    def get(self, request):
        # Get primary resume, or latest resume if no primary exists
        resume = (
            Resume.objects
            .filter(candidate=request.user)
            .order_by("-is_primary", "-uploaded_at")
            .first()
        )

        if not resume:
            return Response({
                "message": "Please upload a resume to get job recommendations.",
                "recommendations": []
            })

        candidate_skills = resume.extracted_skills or []

        if not candidate_skills:
            return Response({
                "message": "No skills found in your resume.",
                "recommendations": []
            })

        jobs = Job.objects.filter(is_active=True)

        recommendations = []

        for job in jobs:
            match_result = calculate_job_match(
                candidate_skills,
                job.skills_required or []
            )

            job_data = JobSerializer(job).data
            job_data.update(match_result)

            recommendations.append(job_data)

        # Sort by highest matching percentage
        recommendations.sort(
            key=lambda item: item["match_percentage"],
            reverse=True
        )

        return Response({
            "candidate_skills": candidate_skills,
            "total_jobs_analyzed": len(recommendations),
            "recommendations": recommendations
        })
