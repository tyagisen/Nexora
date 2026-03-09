from django.db import models

from django.conf import settings
from apps.common.models import BaseModel, SoftDeleteModel
from .choices import OrganizationRole
from .validators import generate_unique_slug

class Organization(BaseModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(blank=True)
    phone =models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    is_active= models.BooleanField(default=True)


    class Meta:
        ordering=["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= generate_unique_slug(Organization, self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Membership(models.Model):
    """
    settings.AUTH_USER_MODEL --> this is done to work even if the user model is customized.
    and use Querying user model i.e. get_user_model()
    Here i used organizations.Organization as it is 
    safer against circular imports
    cleaner in app-based architecture
    common in production django code base.
    """
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='memberships')
    organization = models.ForeignKey("organizations.Organization",on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length=30, choices=OrganizationRole.choices)
    is_active = models.BooleanField(default=True)

    class Meta:
        """
        The constraints supports UniqueConstraint, checkConstraint, conditional rules, expressions, indexes
        So, instead of many old options, Django uses one flexible system.
        """
        #A user could only have One membership in the same organization.
        ordering = ["organization__name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "organization"],
                name="unique_membership"
            )
        ]

    def __str__(self):
        return f"{self.user.email} -- {self.organization.slug} -- {self.role}"