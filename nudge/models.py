from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager
from uuid import UUID, uuid4
from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

class UserManager(DjangoUserManager):
    def get_by_natural_key(self, uuid_or_email):
        if isinstance(uuid_or_email, UUID):
            return self.get(uuid=uuid_or_email)

        try:
            return self.get(uuid=UUID(uuid_or_email))
        except ValueError:
            return self.get(username=uuid_or_email)

    def create_user(self, *args, **kwargs):
        kwargs.pop("username", None)
        username = str(uuid4())
        return super().create_user(username, *args, **kwargs)

    def create_superuser(self, *args, **kwargs):
    	kwargs.pop("username", None)
    	username = str(uuid4())
    	return super().create_superuser(username, *args, **kwargs)


class User(AbstractUser):
    objects = UserManager()
    username = models.CharField(max_length=36, default=uuid4, unique=True)
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField('active', default=True)
    is_admin = models.BooleanField('admin', default=False)

    USERNAME_FIELD = 'username'

    ordering = ('created',)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        db_index=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        db_index=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        db_index=True,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )



class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=25)
    dob = models.CharField(max_length=20)
    #add your fields
    