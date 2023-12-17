from django.db import models

class Profile(models.Model):
    nickname = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f" ({self.nickname})"
