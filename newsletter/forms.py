from django import forms
from .models import NewsLetterUserList, SendEmailToNewsLetterUser
from tinymce import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class NewsLetterUserListForm(forms.ModelForm):
    class Meta:
        model = NewsLetterUserList
        fields = ['email']

    # notice clean_email is nested within Meta Class
"""     def clean_email(self):
        email = self.cleaned_data.get('email')
        return email """


class SendEmailToNewsLetterUserForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCEWidget(
        attrs={'required': False, 'cols': 10, 'rows': 10})
    )

    class Meta:
        model = SendEmailToNewsLetterUser
        fields = ['subject', 'body', 'status']
