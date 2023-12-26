from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3000000), MinValueValidator(0)])
    avatar = models.ImageField(blank=True, upload_to='profile/')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(3000000), MinValueValidator(0)])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username