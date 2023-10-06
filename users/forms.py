from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from mailings.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class UserCustomUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('status',)
