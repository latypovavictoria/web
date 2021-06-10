from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.views.decorators.http import require_POST
from django import conf
from django.contrib.auth.models import User
import time
import jwt
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from app.models import Article
from app.models import Question
from app.models import Answer
from app.models import Author
from app.models import Authoreq
from app.models import User1
from app.models import Tag
from app.forms import LoginForm, QuestionForm, RegisterForm, SettingsForm, AnswerForm
def index(request):
    question=Question.objects.all()
    paginator = Paginator(question, 20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'page': page,'index':posts})
    
@login_required
def ask(request):
    if request.method=="GET":
        form=QuestionForm()
    else:
        form=QuestionForm(data=request.POST)
        if form.is_valid():
            question=form.save(commit=False)
            question.Authoreq=request.user.username
            question.save()
            return redirect(reverse('askqw'))
    return render(request, 'ask.html',{'form':form})
def tag(request):
    titles=Question.objects.all().order_by('?')[:10]
    return render(request, 'tags.html',{})
@login_required
@require_POST
def vote(request):
    rating=model.Question.object.get(pk=1)
    rating.like=F('like')+1
    rating.save()
    data=request.POST
    return JsonResponse(data)
@login_required
def askqw(request):
    answer = Answer.objects.all()
    paginator = Paginator(answer, 20)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    form=AnswerForm(data=request.POST)
    if form.is_valid():
        take_answer=form.save(commit=False)
        take_answer.Author=request.user.username
        take_answer.save()
        return render(request, 'askqw.html',{'page': page,'askqw':posts, 'form':form})
    return render(request, 'askqw.html',{'page': page,'askqw':posts, 'form':form})
def login(request):
    form=LoginForm(data=request.POST)
    if form.is_valid():
        user=auth.authenticate(request, **form.cleaned_data)
        if user is not None:
            auth.login(request, user)
            request.session['Hello']='world'
            return redirect(reverse('askqw')) 
    return render(request, 'login.html',{'form':form})
def logout(request):
    print(request.session.pop('hello', 'nothing'))
    auth.logout(request)
    return redirect(reverse('index'))
def context_processor(request):
    return{
        'rating':cache.get('rating')
    }
def register(request):
    form=RegisterForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        return render(request, 'index.html',{'form':form})
    return render(request, 'register.html',{'form':form})
@login_required
def settings(request):
    form=SettingsForm(data=request.POST, files=request.FILES, instance=request.user)
    if form.is_valid():
        user=form.save(commit=False)
        user.Authoreq=request.user.username
        user.save()
        return render(request, 'settings.html',{'form':form})
    return render(request, 'settings.html',{'form':form})
# Create your views here.
def articles(request):
    articles=Article.objects.all()
    return render(request, 'articles.html',{'articles':articles})
def question(request, qid):
    question=get_object_or_404(models.Question, pk=qid)
    ctx={'question':question}
    if request.user.is_authenticated:
        user_id=str(request.user.pk)
        ctx['cent_token']=jwt.encode({"sub":user_id},
                                    conf.settings.CENTRIFUGO_SECRET_KEY)
        ctx['cent_chan']=f'question_{qid}'
    return render(request, 'question.html',ctx)

 
