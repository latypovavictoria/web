from random import seed
from random import randint
import time
import random
import string 
seed(1)
from django.core.management.base import BaseCommand
from app.models import Author
from app.models import Question
from django.contrib.contenttypes.models import ContentType
def random_string(length):
    word=string.ascii_lowercase
    rand_t=''.join(random.choice(word) for i in range(length))
    return(rand_t)
def str_time(start, end, format, prop):
    stime=time.mktime(time.strptime(start, format))
    etime=time.mktime(time.strtime(end,format))
    ptime=stime+prop*(etime-stime)
    return time.strftime(format, time.localtime(ptime))
def random_date(start, end, prop):
    return str_time(start, end, '%Y-%m-%d', prop)
class Command(BaseCommand):
    help='INSERT!'
    def handle(self, *args, **options):
        from django.db import connection
        cursor=connection.cursor()
        MIN=Author.objects.first().id;
        MAX=Author.objects.last().id;
        for i in range(3):
            q=Question(title=random_string(15), text=random_string(50), tags=random_string(10), date=random_date("2002-01-01", "2021-05-04", random.random()),like=randint(-10000,10000),author=User.objects.get(pk=randint(MIN,MAX)))
            q.save()
