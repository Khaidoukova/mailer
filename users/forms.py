from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.crypto import get_random_string


from mailsender.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.email_confirm_key:
            user.email_confirm_key = get_random_string(length=8)
        if commit:
            user.save()
        return user


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "phone", "country", "avatar"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
