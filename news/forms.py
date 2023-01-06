from django import forms

from .models import Category, News

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