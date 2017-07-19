from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    author = models.CharField(User)
    likes = models.TextField(User)
    
class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass
        
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    author = models.CharField()
    question = models.ForeignKey(Question)
