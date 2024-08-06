import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from .managers import UserManager  # Assuming you have a UserManager to handle your custom user logic


def validate_national_code(value):
    # Check if the national code consists of exactly 10 digits
    if not re.match(r'^\d{10}$', value):
        raise ValidationError(
            '%(value)s is not a valid national code. It must be exactly 10 digits.',
            params={'value': value},
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    nationalCode = models.CharField(
        max_length=10,
        unique=True,
        validators=[validate_national_code],
        verbose_name="National Code",
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Email Address"
    )
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone number")
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True, verbose_name="Mobile number")
    firstName = models.CharField(max_length=255, blank=True, null=True, verbose_name="First Name")
    lastName = models.CharField(max_length=255, blank=True, null=True, verbose_name="Last Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Staff Status"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active Status"
    )
    is_verified = models.BooleanField(default=False, verbose_name="Verification Status")
    last_login = models.DateTimeField(blank=True, null=True, verbose_name="Last Login")

    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Created"
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Date Updated"
    )

    REQUIRED_FIELDS = []  # Required fields for user creation
    USERNAME_FIELD = 'nationalCode'  # Field to use for user authentication

    objects = UserManager()  # Custom user manager

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Changed related_name
        blank=True,
        verbose_name="Groups"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Changed related_name
        blank=True,
        verbose_name="User Permissions"
    )

    def __str__(self):
        return self.nationalCode

    class Meta:
        db_table = 'custom_user'  # Custom table name
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
        ordering = ['create_date']  # Default ordering


class User(AbstractBaseUser, PermissionsMixin):
    nationalCode = models.CharField(
        max_length=10,
        unique=True,
        validators=[validate_national_code],

    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,

    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True, unique=True)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)  # Include last_login field
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False
    )  # Boolean field to indicate if user is staff or
    is_active = models.BooleanField(
        default=True
    )  # Boolean field to indicate if user is active or not

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='Custom_user_groups',  # Change to a unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Change to a unique related_name
        blank=True
    )

    class Meta:
        managed = False  # No migrations will be created for this model
        db_table = 'User'  # Specify the custom table name here

    def __str__(self):
        return self.nationalCode

