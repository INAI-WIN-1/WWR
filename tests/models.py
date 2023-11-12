from django.db import models


class Test(models.Model):
    LEVEL_QUESTION = (
        ('EASY', 'EASY'),
        ('MEDIUM', 'MEDIUM'),
        ('HARD', 'HARD'),
    )
    question = models.CharField(max_length=100)
    answers = models.TextField()
    correct_answer = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_QUESTION, default='EASY')

    def __str__(self):
        return self.question
