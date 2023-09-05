from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class PostForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    text = forms.CharField(widget=forms.Textarea, required=False)