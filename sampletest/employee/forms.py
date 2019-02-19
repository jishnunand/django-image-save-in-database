from django import forms
from django.contrib.auth.models import User
from .models import GENDER

class LoginForm(forms.Form):
	username = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address','required':'required', 'autofocus': 'autofocus'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if username:
			try:
				user = User.objects.get(username=username)
			except User.DoesNotExist:
				raise forms.ValidationError("User not Registered with Us")
		else:
			raise forms.ValidationError("Enter Valid Username")
		return username


class EmployeeForm(forms.Form):
	employee_fname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_lname= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_address= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_phone= forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_gender= forms.ChoiceField(choices=GENDER ,widget=forms.Select(attrs={'class': 'form-control', 'placeholder': ''}))
	employee_image= forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': ''}))
