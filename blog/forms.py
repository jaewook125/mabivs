from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # title = forms.CharField(required=False, widget=forms.TextInput(attrs={
	# 	'class':'form-control',
	# }))
    # content = forms.CharField(required=False, widget=forms.Textarea(attrs={
	# 	'class':'form-control',
	# }))
    # image = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ('title','content','image',)
