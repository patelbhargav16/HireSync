from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/candidate/", include("candidates.urls")),
    path("api/v1/recruiter/", include("recruiters.urls")),
    path("api/v1/jobs/", include("jobs.urls")),
    path("api/v1/resumes/", include("resumes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )