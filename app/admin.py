from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from app.models import Article, Author
from app.models import Question
from app.models import Answer
from app.models import Tag
from app.models import Authoreq
from app.models import User1
admin.site.register(Article)
admin.site.register(User1)
admin.site.register(Author)
admin.site.register(Authoreq)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)