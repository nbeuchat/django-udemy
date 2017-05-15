from django import forms
from blog.models import Post,Comment

class PostForm(forms.modelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.TextArea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.modelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author'=forms.TextInput(attrs={'class':'textinputclass'}),
            'text'=forms.TextArea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
