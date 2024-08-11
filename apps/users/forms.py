from django.core.exceptions import ValidationError
from django.forms import CharField, ModelForm, Form

from .models import User


class UserLoginForm(Form):
    username = CharField(max_length=28)
    password = CharField(max_length=28)


class UserRegisterForm(ModelForm):
    password1 = CharField(max_length=28)
    password2 = CharField(max_length=28)

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError('[!] Passwords must be match')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class UserUpdateForm(ModelForm):
    password1 = CharField(max_length=28)
    password2 = CharField(max_length=28)

    def save(self, commit=True):
        user = super().save(commit=False)
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError('[!] Passwords must match')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
