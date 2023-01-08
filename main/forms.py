from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ListaDeQuestoes(forms.Form):
    def __init__(self, choices=None, *args, **kwargs):
        super(ListaDeQuestoes, self).__init__(*args, **kwargs)
        if choices:
            for c in choices:
                self.fields[c] = forms.IntegerField(
                    initial=0, label=c)
