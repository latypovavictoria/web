from random import seed
from random import randint
import random
import string 
seed(1)
from django.core.management.base import BaseCommand

from app.models import Author
from django.contrib.contenttypes.models import ContentType
def random_string(length):
    word=string.ascii_lowercase
    rand_name=''.join(random.choice(word) for i in range(length))
    return(rand_name)
class Command(BaseCommand):
    help='INSERT!'
    def handle(self, *args, **options):
        from django.db import connection
        cursor=connection.cursor()
        for i in range(9997):
            u=Author(name=random_string(16), birth_date='1996-04-05')
            u.save()
    def handle2(self, *args, **options):
        rating=Author.objects.rating()
        cache.set('rating': rating, 86400+3600)
            