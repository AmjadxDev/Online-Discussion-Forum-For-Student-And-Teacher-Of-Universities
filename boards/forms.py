from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder':'Subject belongs to Topic Model'}), max_length=40)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Message belongs to Post Model'}), max_length=4000, help_text='The max length of the text is 4000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]