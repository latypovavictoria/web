from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import Question
from app.models import Author
from app.models import Authoreq
from app.models import User1
from app.models import Answer
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['title', 'text', 'tags']
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class SettingsForm(forms.ModelForm):
    avatar=forms.ImageField()
    class Meta:
        model=Authoreq
        fields=['email', 'password', 'avatar']
    def save(self, *args, **kwargs):
        user=super().save(*args, **kwargs)
        user.authore.avatar=self.cleaned_data['avatar']
        user.authore.save()
        return user
class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['text']