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
        fields = ['rut', 'nombre', 'correo' , 'telefono', 'direccion', 'contraseña']
        labels ={
            'rut': 'rut', 
            'nombre': 'Nombre', 
            'correo': 'Correo',
            'telefono': 'telefono',
            'direccion': 'direccion',
            'contraseña': 'contraseña'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono',
                    'id': 'telefono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion',
                    'id': 'direccion',
                }
            ),
            'contraseña': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña',
                    'id':'contraseña'
                }
            ),

        }


class LoginForm(forms.ModelForm):

    class Meta: 
        fields = ['correo', 'contraseña']
        labels ={
            'correo': 'Correo',
            'contraseña': 'contraseña'
        }
        widgets={
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ), 
            'contraseña': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña',
                    'id':'contraseña'
                }
            ),

        }

 
