
from django.db import models
from django.conf import settings


class CandidateProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="candidate_profile",
    )

    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=150, blank=True)
    headline = models.CharField(max_length=255, blank=True)
    professional_summary = models.TextField(blank=True)

    skills = models.JSONField(default=list, blank=True)
    years_of_experience = models.PositiveIntegerField(default=0)

    current_position = models.CharField(max_length=150, blank=True)
    education = models.TextField(blank=True)

    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Candidate Profile - {self.user.email}"
