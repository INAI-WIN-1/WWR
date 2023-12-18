from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(3000000), MinValueValidator(0)])

    def __str__(self):
        return self.user.username