from django import forms
from .models import Post

# PostForm é o nome do nosso formulario
class PostForm(forms.ModelForm):
	# Determina o model qué seŕa usado
	# Determina os campos que serão expostos
	class Meta:
		model = Post
		fields = ('title', 'text')