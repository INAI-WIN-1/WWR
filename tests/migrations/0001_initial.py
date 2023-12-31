# Generated by Django 4.2.7 on 2023-11-24 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answers', models.TextField()),
                ('correct_answer', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('EASY', 'EASY'), ('MEDIUM', 'MEDIUM'), ('HARD', 'HARD')], default='EASY', max_length=50)),
            ],
        ),
    ]
