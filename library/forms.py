from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 获取当前的用户模型
MyUser = get_user_model()


class UserForm(forms.ModelForm):
    """
    UserForm 是一个 ModelForm，用于处理用户的邮箱字段。
    它包含一个 Meta 类，定义了表单的一些元数据。
    """

    class Meta:
        model = User  # 使用 Django 的内置 User 模型
        fields = ['email']  # 表单包含的字段
        labels = {
            'email': '邮箱',  # 字段的标签
        }
        help_texts = {
            'email': '请输入您的邮箱',  # 字段的帮助文本
        }
        error_messages = {
            'email': {
                'required': '邮箱不能为空',  # 当字段为空时的错误消息
                'invalid': '邮箱格式不正确',  # 当字段格式不正确时的错误消息
            },
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # 字段的小部件
        }


class CustomUserCreationForm(UserCreationForm):
    """
    CustomUserCreationForm 是一个 UserCreationForm 的子类，用于处理用户的注册。
    它添加了一个必填的 email 字段，并使用自定义的用户模型。
    """

    email = forms.EmailField(required=True)  # 添加一个必填的 email 字段

    class Meta:
        model = MyUser  # 使用自定义的用户模型
        fields = ('username', 'email', 'password1', 'password2')  # 表单包含的字段
