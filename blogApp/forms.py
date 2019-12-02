from django import forms
from tinymce import TinyMCE
from .models import Post


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=TinyMCEWidget(
        attrs={'required': False, 'cols': 10, 'rows': 10})
    )
    thumbnail = forms.ImageField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'thumbnail']
