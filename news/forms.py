from django import forms

from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя:', help_text="Имя пользователя должно состоять максимум из 150 символов", widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтверждение пароля:', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username','email', 'password1',  'password2')
        # так почему-то не работает
        # widgets = {
        #     'username': forms.TextInput(attrs={"class": "form-control"}),
        #     'email': forms.EmailInput(attrs={"class": "form-control"}),
        #     'password1': forms.PasswordInput(attrs={"class": "form-control"}),
        #     'password1': forms.PasswordInput(attrs={"class": "form-control"}),
        # }



# Для несвязанный с моделью форм
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#     is_publishes = forms.BooleanField(label='Опубликовано?', initial=True)
#     category = forms.ModelChoiceField(empty_label='Выбирите категорию', queryset=Category.objects.all(), label='Категория', widget=forms.Select(attrs={"class": "form-control"}))


# Для связанных с моделью форм
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_publishes', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
