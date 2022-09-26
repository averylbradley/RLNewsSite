#from xml.etree.ElementTree import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class PostForm(forms.ModelForm):
	body = forms.CharField(
		required=True,
		widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Type something...",
                "class": "textarea is-success is-medium",
            }
        ),
    	label="",
	)

	class Meta:
		model = Post
		exclude = ("user",)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.TextInput(attrs={'class': 'form-control'})
		}

