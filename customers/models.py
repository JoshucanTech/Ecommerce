# accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Custom Manager to handle user creation
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """Create and return a regular user with an email, username, and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """Create and return a superuser with an email, username, and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email field
    username = models.CharField(max_length=150, unique=True)  # Username field
    first_name = models.CharField(max_length=30, blank=True)  # Optional first name
    last_name = models.CharField(max_length=30, blank=True)  # Optional last name
    address = models.TextField(max_length=555, blank=True)  # Optional Address
    date_joined = models.DateTimeField(default=timezone.now)  # Date when user joined
    last_login = models.DateTimeField(auto_now=True)  # Last login time
    is_active = models.BooleanField(default=True)  # Whether the user is active
    is_staff = models.BooleanField(default=False)  # Whether the user is a staff member
    is_superuser = models.BooleanField(default=False)  # Whether the user is a superuser

   
    objects = CustomUserManager()  # Use the custom manager

    USERNAME_FIELD = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['username']  # Fields required when creating a superuser

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
