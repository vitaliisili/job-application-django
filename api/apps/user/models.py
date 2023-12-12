import uuid
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db import models
from django_cleanup import cleanup


class UserManager(BaseUserManager):
    """A custom user manager for creating and managing user accounts.
    Methods:
        create_user: Creates and saves a new user.
        create_superuser: Creates and saves a new superuser.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user.
        Args:
            email (str): The email address of the user.
            password (str, optional): The password for the user. Default is None.
            **extra_fields: Additional fields for the user.
        Returns:
            User: The newly created user.
        Raises:
            ValueError: If the email is not provided.
        Notes:
            This method creates a new user, normalizes the email address, sets the password, and saves the user.
        """

        if not email:
            raise ValueError('User must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser.
        Args:
            email (str): The email address of the superuser.
            password (str): The password for the superuser.
        Returns:
            User: The newly created superuser.
        Note:
            This method creates a new superuser by calling the create_user method and setting additional attributes.
        """

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


@cleanup.select
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system.
    Attributes:
        email (EmailField): The email address of the user. Max length is 255 characters. Must be unique.
        name (CharField): The name of the user. Max length is 255 characters.
        is_active (BooleanField): Indicates if the user is active. Default is True.
        is_staff (BooleanField): Indicates if the user is a staff member. Default is False.
        role (ForeignKey): The role of the user, linked to the Role model.
        created_at (DateTimeField): The date and time when the user was created. Auto-generated and not editable.
        updated_at (DateTimeField): The date and time when the user was last updated. Auto-generated.
        image (ImageField): The profile picture of the user. Can be null.
        is_verified (BooleanField): Indicates if the user is verified. Default is False.
        objects (UserManager): The user manager object for creating and managing user accounts.
        USERNAME_FIELD (str): The field used as the unique identifier for the user.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        """Returns the name of the user.
        Returns:
            str: The name of the user.
        """
        return self.name
