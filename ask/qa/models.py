from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()
    added_at = models.DateField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField()
    
class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass
        
        
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    author = models.ForeignKey(User, max_length = 30)
    question = models.ForeignKey(Question)
