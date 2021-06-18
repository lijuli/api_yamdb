from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from .utils import get_random_code

CHOICES = (
    ('USER', 'user'),
    ('MODERATOR', 'moderator'),
    ('ADMIN', 'admin'),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, username):
        user = self.create_user(
            email,
            password=password,
            username=username,
            role=CHOICES[1][1],
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            role=CHOICES[2][1],
        )
        user.staff = True
        user.superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20, unique=True, blank=False, null=False
    )
    password = models.CharField(max_length=128, blank=True, null=True)
    bio = models.TextField(
        max_length=1000, null=True, blank=True, verbose_name='Рассказ о себе'
    )
    role = models.CharField(
        max_length=15,
        choices=CHOICES,
        default='USER',
        verbose_name='Роль',
    )
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False
    )
    confirmation_code = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        default=get_random_code(10),
        verbose_name='Код подтверждения',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    @property
    def is_superuser(self):
        return self.role == 'admin'

    @property
    def is_staff(self):
        return self.role == 'moderator'


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, username, password, **kwargs):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             **kwargs
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password, username):
#         user = self.create_user(
#             email,
#             password=password,
#             username=username
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, username):
#         user = self.create_user(
#             username=username,
#             email=email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user


# class CustomUser(AbstractUser):
#     class Roles(models.TextChoices):
#         USER = 'user'
#         MODERATOR = 'moderator'
#         ADMIN = 'admin'

#     username = models.CharField(
#         max_length=20, unique=True, blank=False, null=False
#     )
#     bio = models.TextField(
#         max_length=1000, null=True, blank=True, verbose_name='Рассказ о себе'
#     )
#     role = models.CharField(
#         max_length=15,
#         choices=Roles.choices,
#         default=Roles.USER,
#         verbose_name='Роль',
#     )
#     email = models.EmailField(
#         max_length=255, unique=True, blank=False, null=False
#     )
#     confirmation_code = models.CharField(
#         max_length=10,
#         null=True,
#         blank=True,
#         default=get_random_code(10),
#         verbose_name='Код подтверждения',
#     )

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ('email', 'password')

#     @property
#     def is_admin(self):
#         return self.role == self.Roles.ADMIN

#     @property
#     def is_staff(self):
#         return self.role == self.Roles.MODERATORz
