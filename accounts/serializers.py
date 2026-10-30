
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BaseRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CandidateRegistrationSerializer(BaseRegistrationSerializer):
    def create(self, validated_data):
        validated_data["role"] = User.Role.CANDIDATE
        return super().create(validated_data)


class RecruiterRegistrationSerializer(BaseRegistrationSerializer):
    def create(self, validated_data):
        validated_data["role"] = User.Role.RECRUITER
        return super().create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data["user"] = {
            "id": self.user.id,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "role": self.user.role,
        }

        return data
