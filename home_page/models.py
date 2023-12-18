from django.db import models

class HomePage(models.Model):
    image = models.ImageField(upload_to='main/')
    title = models.CharField(max_length=50)
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()
    text5 = models.TextField()
    text6 = models.TextField()