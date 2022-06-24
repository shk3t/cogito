from django import forms
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

from base.models import Source, Cluster


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
    # class Meta:
    #     model = User
    #     fields = ["username", "password"]


class SourceForm(forms.Form):
    name = forms.CharField(max_length=64)
    description = forms.CharField(widget=forms.Textarea)
    content = forms.FileField(
        required=False, validators=[FileExtensionValidator(allowed_extensions=["md"])]
    )
    cluster = forms.ModelChoiceField(queryset=Cluster.objects.all(), required=False)
    # class Meta:
    #     model = Source
    #     fields = "__all__"
    #     exclude = ["user"]


# class SourceForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField(widget=forms.Textarea)
#    cluster = forms.ModelChoiceField(Cluster.objects.all(), required=False)


class MessageForm(forms.Form):
    body = forms.CharField(label="", widget=forms.Textarea)
