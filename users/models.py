from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .utils import get_random_code


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **kwargs
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    username = models.CharField(
        max_length=20, unique=True, blank=False, null=False
    )
    bio = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name='Рассказ о себе'
    )
    role = models.CharField(
        max_length=15,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name='Роль',
    )
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False
    )
    confirmation_code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        default=get_random_code(10),
        verbose_name='Код подтверждения',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    @property
    def is_superuser(self):
        return self.role == self.Roles.ADMIN

    @property
    def is_staff(self):
        return self.role == self.Roles.MODERATOR
