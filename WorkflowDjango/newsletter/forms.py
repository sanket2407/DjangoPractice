from django import forms

from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']
		#exclude = ['full_name']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		print email
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Enter valid email having .edu extension")
		return email