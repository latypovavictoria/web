from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from random import shuffle
import time
from users import Command
f=Command()
class AuthorManager(models.Manager):
    def rating(self):
    lst=list(range(1,11))
    shuffle(lst)
    time.sleep(4)
    return [
        {'username': f.name(), 'user_id': i} for i in lst(10)
    ]
class Author(models.Model):
    name=models.CharField(max_length=255)
    birth_date=models.DateField()
    def __str__(self):
        return self.name
    objects=AuthorManager()
class User1(models.Model):
    username=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=60)
    firstname=models.CharField(max_length=60, default=None)
    lastname=models.CharField(max_length=60, default=None)
    def __str__(self):
        return self.username 
class Authoreq(models.Model):
    username=models.CharField(max_length=60)
    email=models.EmailField(max_length=60)
    password=models.CharField(max_length=60)
    avatar=models.ImageField(upload_to='avatar/', default='1.jpg')
    login=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.username 
class ArticleManager(models.Manager):
    def only_from_kristina(self):
        return self.filter(author_id=2)
        
        
class Article(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    objects=ArticleManager()
    def __str__(self):
        return self.title

class Question(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    text=models.TextField()
    tags=models.CharField(max_length=60)
    date=models.DateField(default=datetime.now)
    like=models.IntegerField(default=0,null=False)
    author=models.ForeignKey('Authoreq',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Answer(models.Model):
    title=models.ForeignKey('Question',on_delete=models.CASCADE)
    text=models.TextField()
    date=models.DateField(default=datetime.now)
    like=models.IntegerField(default=0,null=False)
    author=models.ForeignKey('Authoreq',on_delete=models.CASCADE)
    def __str__(self):
        return self.text
class Tag(models.Model):
    id_t=models.PositiveIntegerField()
    title=models.ForeignKey('Question',on_delete=models.CASCADE)
    def __int__(self):
        return self.id_t