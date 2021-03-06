from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']


class MemberForm(ModelForm):
	class Meta:
		model = Member
		fields = '__all__'
		exclude = ['user']