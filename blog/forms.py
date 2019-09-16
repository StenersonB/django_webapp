from django import forms
from .models import Post, Image

class PostCreationForm(forms.ModelForm):
	title = forms.CharField()
	post_type = forms.ChoiceField(choices=Post.POST_TYPES)
	content = forms.Textarea()

	class Meta:
		model = Post
		fields = ['title', 'post_type', 'content']

class ImageForm(forms.ModelForm):
	image = forms.ImageField(label='Image')

	class Meta: 
		model = Image
		fields = ['image']