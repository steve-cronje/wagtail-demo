from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_email(self):
		data = self.cleaned_data['email']
		if User.objects.filter(email=data).exists():
			raise forms.ValidationError("There is already a user with that email!")
		
		return data
		

class LoginForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_email(self):
		data = self.cleaned_data['email']
		if not User.objects.filter(email=data).exists():
			raise forms.ValidationError("There is no user registered with that email!")
		
		return data
