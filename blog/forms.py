from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = Post
        fields = ('title','content',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','message',)
