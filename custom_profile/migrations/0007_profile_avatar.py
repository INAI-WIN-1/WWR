# Generated by Django 5.0 on 2023-12-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_profile', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profile/'),
        ),
    ]