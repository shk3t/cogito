from django import forms
from django.contrib.auth.models import User

from .models import Source, Cluster


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
#    class Meta:
#        model = User
#        fields = ["username", "password"]


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ["name", "description", "cluster"]


#class SourceForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField(widget=forms.Textarea)
#    cluster = forms.ModelChoiceField(Cluster.objects.all(), required=False)


class MessageForm(forms.Form):
    body = forms.CharField(label="", widget=forms.Textarea)
