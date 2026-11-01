from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):

    recruiter_email = serializers.EmailField(
        source="recruiter.email",
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            "id",
            "recruiter_email",
            "title",
            "company_name",
            "location",
            "description",
            "requirements",
            "skills_required",
            "job_type",
            "experience_level",
            "salary_min",
            "salary_max",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "recruiter_email",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        salary_min = data.get(
            "salary_min",
            getattr(self.instance, "salary_min", None)
        )
        salary_max = data.get(
            "salary_max",
            getattr(self.instance, "salary_max", None)
        )

        if (
            salary_min is not None
            and salary_max is not None
            and salary_min > salary_max
        ):
            raise serializers.ValidationError(
                "Minimum salary cannot be greater than maximum salary."
            )

        return data