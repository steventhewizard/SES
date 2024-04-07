from django.db import models

class Essay(models.Model):
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    essay_text = models.TextField()

class Rubric(models.Model):
    title = models.CharField(max_length=100)
    criteria = models.TextField()