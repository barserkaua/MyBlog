
from .models import Article
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date',  'user']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name state'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date publish',
            }),
            "user": TextInput(attrs={
                'class': 'form-control',
                'value': 'Username',
                'id': 'user',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Some text...',
            }),
        }