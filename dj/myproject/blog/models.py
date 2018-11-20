from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=63)
class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)