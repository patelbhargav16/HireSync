
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import (
    CandidateRegistrationSerializer,
    RecruiterRegistrationSerializer,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import IsCandidate, IsRecruiter


class CandidateDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsCandidate]

    def get(self, request):
        return Response({
            "message": "Welcome to the Candidate Dashboard!",
            "email": request.user.email,
            "role": request.user.role,
        })


class RecruiterDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsRecruiter]

    def get(self, request):
        return Response({
            "message": "Welcome to the Recruiter Dashboard!",
            "email": request.user.email,
            "role": request.user.role,
        })


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer



class CandidateRegistrationView(generics.CreateAPIView):
    serializer_class = CandidateRegistrationSerializer
    permission_classes = [AllowAny]


class RecruiterRegistrationView(generics.CreateAPIView):
    serializer_class = RecruiterRegistrationSerializer
    permission_classes = [AllowAny]
