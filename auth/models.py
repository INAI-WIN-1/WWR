from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
# class SimpleUser(AbstractUser):
#     pass

# class Game(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     status = models.BooleanField()
#     rating = models.PositiveIntegerField(validators=[MaxValueValidator(3000000), MinValueValidator(0)])
#     question = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.user