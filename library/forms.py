from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

MyUser = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
        labels = {
            'email': '邮箱',
        }
        help_texts = {
            'email': '请输入您的邮箱',
        }
        error_messages = {
            'email': {
                'required': '邮箱不能为空',
                'invalid': '邮箱格式不正确',
            },
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'password1', 'password2')
