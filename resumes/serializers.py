import pymupdf
from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):

    file = serializers.FileField(write_only=True, required=True)

    class Meta:
        model = Resume
        fields = [
            "id",
            "file",
            "original_filename",
            "extracted_text",
            "extracted_skills",
            "is_primary",
            "uploaded_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "original_filename",
            "extracted_text",
            "extracted_skills",
            "uploaded_at",
            "updated_at",
        ]

    def validate_file(self, file):
        if not file.name.lower().endswith(".pdf"):
            raise serializers.ValidationError("Only PDF files are allowed.")

        if file.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("PDF file size must not exceed 5MB.")

        if not file.read(5).startswith(b"%PDF-"):
            raise serializers.ValidationError("Invalid PDF file.")

        file.seek(0)

        try:
            document = pymupdf.open(
                stream=file.read(),
                filetype="pdf"
            )

            if document.is_encrypted:
                document.close()
                raise serializers.ValidationError(
                    "Password-protected PDFs are not allowed."
                )

            document.close()

        except serializers.ValidationError:
            raise
        except Exception:
            raise serializers.ValidationError("Unable to read this PDF file.")

        file.seek(0)
        return file