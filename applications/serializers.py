
from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    job_title = serializers.CharField(
        source="job.title",
        read_only=True
    )

    company_name = serializers.CharField(
        source="job.company_name",
        read_only=True
    )

    candidate_email = serializers.EmailField(
        source="candidate.email",
        read_only=True
    )

    class Meta:
        model = Application
        fields = [
            "id",
            "candidate",
            "candidate_email",
            "job",
            "job_title",
            "company_name",
            "cover_letter",
            "status",
            "applied_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "candidate",
            "status",
            "applied_at",
            "updated_at",
        ]


class ApplicationStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ["status"]
