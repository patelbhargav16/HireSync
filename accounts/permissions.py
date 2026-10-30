
from rest_framework.permissions import BasePermission


class IsCandidate(BasePermission):
    message = "Only candidates can access this resource."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "CANDIDATE"
        )


class IsRecruiter(BasePermission):
    message = "Only recruiters can access this resource."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "RECRUITER"
        )
