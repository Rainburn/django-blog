from django import forms
from .models import Blog, Author, Entry
from django.core.validators import validate_slug
from .utils import *

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('blog', 'headline', 'body_text', 'authors', 'number_of_comments', 'number_of_pingbacks')

    blog = forms.ModelChoiceField(queryset=Blog.objects.all(), required=True)
    number_of_comments = forms.IntegerField(min_value=0)
    number_of_pingbacks = forms.IntegerField(min_value=0)
    body_text = forms.CharField(widget=forms.Textarea, required=False)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'email', 'password')


    name = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data["name"]
        password = cleaned_data["password"]

        special_chars = '#@%^&*!?_<>'

        if (password != ""):
            if name.lower() in password.lower():
                raise forms.ValidationError("Password should not contain name")
        
            if (not contain_alphanumeric(password)):
                raise forms.ValidationError("Password must contain alphabet and numeric")

            regex_special_chars = '[' + special_chars + ']'
            if (not contain_special_chars(password, regex_special_chars)):
                raise forms.ValidationError(("Password must contain special character such as %(special_chars)s"),
                                            params={"special_chars": special_chars})