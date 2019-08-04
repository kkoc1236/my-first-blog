from django import forms
from .models import Document, Comment
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post

class Buttonform(forms.Form):
    btn = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    #text = forms.TextInput(label = '댓글')

    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].label = "Comment"