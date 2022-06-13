from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Producto, Cliente


class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen']
        labels ={
            'nombre': 'Nombre', 
            'precio': 'precio', 
            'descripcion': 'descripcion',
            'imagen': 'imagen'
        }
        # widgets={
        #     'nombre': forms.TextInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'Ingrese nombre', 
        #             'id': 'nombre'
        #         }
        #     ), 
        #     'precio': forms.TextInput(
        #         attrs={
        #             'class': 'form-control', 
        #             'placeholder': 'Ingrese precio', 
        #             'id': 'precio'
        #         }
        #     ), 
        #     'descripcion': forms.TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Ingrese descripcion',
        #             'id': 'descripcion',
        #         }
        #     ),
        #     'imagen': forms.ImageField(
        #         attrs={
        #             'upload_to': '/images'
        #         }
        #     )

        # }

class ClienteForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['nombre', 'rut', 'direccion', 'telefono']
        labels ={
            'nombre': 'Nombre', 
            'rut': 'rut', 
            'direccion': 'direccion',
            'telefono': 'telefono',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion',
                    'id': 'direccion',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono',
                    'id': 'telefono',
                }
            )

        }

 
    
     

