# Generated by Django 5.0 on 2023-12-20 18:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
