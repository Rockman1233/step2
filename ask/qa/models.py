from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        pass
    def popular(self):
        pass

class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length = 30)
    text = models.TextField(default="")
    added_at = models.DateField(auto_now_add = True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name="q_to_likes")
            
class Answer(models.Model):
    text = models.TextField(default="")
    added_at = models.DateField()
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
