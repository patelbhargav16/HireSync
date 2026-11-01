
from rest_framework import serializers
from .models import RecruiterProfile


class RecruiterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruiterProfile
        exclude = ["user", "created_at", "updated_at"]
        read_only_fields = ["id"]
