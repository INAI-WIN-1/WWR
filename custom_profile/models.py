from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from main import settings


class CustomUser(AbstractUser):
    balance = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3000000), MinValueValidator(0)])
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Game(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(3000000), MinValueValidator(0)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username