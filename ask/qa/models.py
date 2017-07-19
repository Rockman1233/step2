from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    author = models.CharField()
    likes = models.TextField()

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    author = models.CharField()
    question = models.ForeignKey(Question)
