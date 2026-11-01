import pymupdf

from django.db import transaction
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Resume
from .serializers import ResumeSerializer
from .services import extract_skills
from accounts.permissions import IsCandidate


class ResumeListCreateView(generics.ListCreateAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsCandidate]

    def get_queryset(self):
        return Resume.objects.filter(candidate=self.request.user)

    def perform_create(self, serializer):
        uploaded_file = self.request.FILES["file"]

        document = pymupdf.open(
            stream=uploaded_file.read(),
            filetype="pdf"
        )

        extracted_text = "\n".join(
            page.get_text() for page in document
        )

        document.close()
        uploaded_file.seek(0)

        extracted_skills = extract_skills(extracted_text)

        serializer.save(
            candidate=self.request.user,
            original_filename=uploaded_file.name,
            extracted_text=extracted_text,
            extracted_skills=extracted_skills
        )


class ResumeDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, IsCandidate]

    def get_queryset(self):
        return Resume.objects.filter(candidate=self.request.user)