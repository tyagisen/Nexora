from django.db import models

class OrganizationRole(models.TextChoices):
    OWNER = "owner", "Owner"
    COUNSELLOR = "counsellor", "Counsellor"
    STUDENT = "student", "Student"