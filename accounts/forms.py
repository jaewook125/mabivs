from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
	username = forms.RegexField(label="Username", max_length=30,
	regex=r'^[\w.@+-]+$',
	help_text="Required! 30 characters or fewer. Letters, digits and "
	"@/./+/-/_ only.",
	error_messages={
	'invalid': "아이디는 영어, 숫자, @ . + - _ 만 사용하실 수 있습니다."},
	widget=forms.TextInput(attrs={
	'class': 'form-control',
	'placeholder': '웹에서 사용할 아이디입니다',
	'required': 'true',
	}))
	password1 = forms.CharField(label="Password",
	widget=forms.PasswordInput(attrs={
	'class': 'form-control',
	'placeholder': '패스워드',
	'required': 'true',
	}))
	password2 = forms.CharField(label="Password confirmation",
	widget=forms.PasswordInput(attrs={
	'class': 'form-control',
	'placeholder': '패스워드 재확인',
	'required': 'true',
	}))
	class Meta:
		model = User
		fields = ("username", "password1", "password2",)

class LoginForm(AuthenticationForm):
	username = forms.CharField(
		max_length=254,
		widget=forms.TextInput(
		attrs={
		'class': 'form-control',
		'placeholder': 'Username',
		'required': 'True',
	}))
	password = forms.CharField(
		widget=forms.PasswordInput(
		attrs={
		'class': 'form-control',
		'placeholder': 'Password',
		'required': 'True',
	}))


class MypageForm(forms.Form):
	CHOICES=[('울프','울프'),
			('하프','하프'),
			('류트','류트'),
         ('만돌린','만돌린')]

	RACE_CHOICES=[('인간','인간'),
			('엘프','엘프'),
			('자이언트','자이언트')]

	SKILL_CHOICES=[('근접 전투','근접 전투'),
			('랜스','랜스'),
			('궁술','궁술'),
			('마법','마법'),
			('격투술','격투술'),
         	('연금술','연금술'),
		 	('올라운더','올라운더')]

	userid = forms.CharField(required=False, widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder': 'ex)MD은단비,LT놀즈,HP하프,WF감투',
	}))
	server = forms.ChoiceField(required=False, choices=CHOICES,widget=forms.Select(attrs={
		'class':'form-control',
	}))
	race = forms.ChoiceField(required=False, choices=RACE_CHOICES,widget=forms.Select(attrs={
		'class':'form-control',
	}))
	skill = forms.ChoiceField(required=False, choices=SKILL_CHOICES,widget=forms.RadioSelect(attrs={
		'class':'form-select',
	}))
	context = forms.CharField(required=False, widget=forms.Textarea(attrs={
		'class':'form-control',
		'placeholder': 'pvp 초보입니다!',
	}))
	image = forms.ImageField()
