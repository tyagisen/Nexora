from django.db import models
from django.conf import settings
from .choices import Gender
from apps.common.models import BaseModel, SoftDeleteModel


class StudentProfile(BaseModel, SoftDeleteModel):
    organization = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE,related_name="students")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="student_profile")
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=Gender.choices)
    nationality = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

    interested_country = models.CharField(max_length=100, blank=True)
    preferred_intake = models.CharField(max_length=100, blank=True)
    
    assigned_counsellor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_students")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.SET_NULL, null=True, blank=True, related_name="created_students")

    class Meta:
        """
        This indexing is really powerful thing :- it is a database optimization method. It make data retrieval faster.
        So, the database can find rows quickly without scanning the entire table.
        """
        ordering = ["-created_at"]
        indexes= [
            models.Index(fields=["organization", "email"]),
            models.Index(fields=["organization", "assigned_counsellor"]),
            models.Index(fields=["organization", "created_at"]),

        ]
    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
