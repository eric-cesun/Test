from django import forms
from .models import Libro,Categoria,Autor
class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=[
        "titulo",
        "imagen",
        "contenido",
        "autor",
        "categoria",
        ]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=[
        "categoria",
        "descripcion",
        ]


class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=[
        "nombreCompleto",
        "imagen",
        "correo",
        "nacionalidad",
        "bibliografia",
        ]
