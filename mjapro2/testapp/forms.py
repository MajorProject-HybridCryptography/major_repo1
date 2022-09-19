from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	#email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	#def save(self, commit=True):
	#	user = super(NewUserForm, self).save(commit=False)
	#	user.email = self.cleaned_data['email']
	#	if commit:
	#		user.save()
	#	return user

class UploadForm(forms.Form):
    select = forms.CharField(label="Select Users",max_length=50)
    image  = forms.FileField(label="File  Upload ")
    file   = forms.FileField(label="Image Upload ") # for creating file input
    email  = forms.EmailField(label="Enter Email")