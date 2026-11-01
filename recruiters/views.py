
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import RecruiterProfile
from .serializers import RecruiterProfileSerializer
from accounts.permissions import IsRecruiter


class RecruiterProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = RecruiterProfileSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get_object(self):
        profile, created = RecruiterProfile.objects.get_or_create(
            user=self.request.user,
            defaults={"company_name": ""},
        )
        return profile
