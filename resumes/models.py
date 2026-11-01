from django.conf import settings
from django.db import models


class Resume(models.Model):

    candidate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="resumes"
    )

    file = models.FileField(upload_to="resumes/")

    original_filename = models.CharField(max_length=255)

    extracted_text = models.TextField(blank=True)

    is_primary = models.BooleanField(default=False)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    extracted_skills = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.original_filename} - {self.candidate.email}"