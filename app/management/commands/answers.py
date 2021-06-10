from random import seed
from random import randint
import time
import random
import string 
seed(1)
from django.core.management.base import BaseCommand
from app.models import Author
from app.models import Question
from app.models import Answer
from django.contrib.contenttypes.models import ContentType
def random_string(length):
    word=string.ascii_lowercase
    rand_t=''.join(random.choice(word) for i in range(length))
    return(rand_t)
def str_time(start, end, format, prop):
    stime=time.mktime(time.strptime(start, format))
    etime=time.mktime(time.strptime(end,format))
    ptime=stime+prop*(etime-stime)
    return time.strftime(format, time.localtime(ptime))
def random_date(start, end, prop):
    return str_time(start, end, '%Y-%m-%d', prop)
class Command(BaseCommand):
    help='INSERT!'
    def handle(self, *args, **options):
        from django.db import connection
        cursor=connection.cursor()
        for i in range(980000):
            a=Answer(
            author=Author.objects.get(name='Michael'),
            title=Question.objects.get(id=randint(1, 100000)),
            text=random_string(50), 
            date=random_date("2002-01-01", "2021-05-04", random.random()),
            like=randint(-10000,10000))
            a.save()