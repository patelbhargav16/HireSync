
from django.db import models
from django.conf import settings


class RecruiterProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recruiter_profile",
    )

    company_name = models.CharField(max_length=200)
    company_website = models.URLField(blank=True)
    designation = models.CharField(max_length=150, blank=True)
    company_description = models.TextField(blank=True)

    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=150, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name} - {self.user.email}"
