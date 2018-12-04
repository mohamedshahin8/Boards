from django import forms
from .models import *

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = {'placeholder': "what's on your mind?"}
        ),
        max_length=4000,
        help_text='The max length of the text is 5000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message' ,]
