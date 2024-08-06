from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


# Custom User Manager
class UserManager(BaseUserManager):
    # Method to create a new user
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("The username must be set"))

        # Directly use the username without normalization
        user = self.model(nationalCode=username, **extra_fields)
        # Set the raw password (do not hash it)

        # Hash the password before saving it
        user.password = make_password(password)

        user.save(using=self._db)
        return user

    # Method to create a new superuser
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, password, **extra_fields)
