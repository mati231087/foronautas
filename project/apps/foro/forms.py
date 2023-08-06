from django import forms
from .models import Tema, Comentario

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'contenido', 'imagen', 'video']  # Incluir aquí los demás campos del modelo Tema

    def __init__(self, *args, **kwargs):
        super(TemaForm, self).__init__(*args, **kwargs)
        self.fields['contenido'].widget = forms.Textarea(attrs={'rows': 5})  # Establecer la estructura del mensaje del tema

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido', 'imagen', 'video']

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['contenido'].widget = forms.Textarea(attrs={'rows': 5})