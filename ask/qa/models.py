from django.db import models

# Create your models here.
class Question(models.Model):
  title = models.CharField()
  text = models.TextField()
  added_at = models.DateField()
  rating = models.FloatField()
  author = models.CharField()
  likes = models.TextField()

class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateField()
  author = models.CharField()
