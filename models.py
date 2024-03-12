from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Specify unique related_name for groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='app1_users',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='app1_users',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
        )
    
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)