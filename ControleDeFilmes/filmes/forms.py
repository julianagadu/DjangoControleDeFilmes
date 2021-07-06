from django import forms
from django.forms import fields, widgets
from .models import Filme

class Filmeform(forms.ModelForm):

    class Meta:
        model = Filme
        fields = ['titulo','lancamento','descricao','duracao','capa','categoria','produtora']
       
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':"form-control", 'placeholder': "Informe o título do filme"}),
            'lancamento' : forms.TextInput(attrs={'class':"form-control", 'placeholder': "Informe o ano de lançamento"}),
            'descricao' : forms.Textarea(attrs={'class':"form-control", 'placeholder': "Breve descrição do filme"}),
            'duracao': forms.TextInput(attrs={'class':"form-control", 'placeholder': "Tempo de duração do filme"}),
            'categoria': forms.Select(attrs={'class':"form-control"}),
            'produtora': forms.Select(attrs={'class':"form-control"}),
            'capa': forms.FileInput
            
        }

        error_messages = {
            'titulo': { 'required': 'O campo título é obrigatório'}
        }

