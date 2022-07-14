from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

class CreateUserForm(UserCreationForm):

    username =  forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Ingrese username', 
            'type': 'username'
          }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Ingrese email',
            'type':'email'
        }
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'first_name',
            'placeholder': 'Ingrese nombres', 
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'last_name',
            'placeholder':('Last Name')
        }
    ))

    password1 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            'placeholder':'Ingrese Contraseña',
        }
    ))
    password2 = forms.CharField(max_length=16,widget=forms.PasswordInput(
        attrs={
            'placeholder':'Repita Contraseña',
        }
    ))
    class Meta: 
        model= User
        fields = ['username','email','first_name','last_name','password1','password2']



class LoginForm(forms.ModelForm):

    class Meta: 
        model= Cliente
        fields = ['rut', 'password1']
        labels ={
            'rut': 'rut',
            'password1': 'password1'
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'password1': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese contraseña',
                    'id':'contraseña'
                }
            ),

        }

class ClienteForm(UserCreationForm):
    
    rut = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'rut',
            'placeholder':('rut')
        }
    ))
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'nombre',
            'placeholder':('nombre')
        }
    )) 
    correo = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'correo',
            'placeholder':('correo')
        }
    ))
    telefono = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'telefono',
            'placeholder':('telefono')
        }
    ))
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={
            'type':'direccion',
            'placeholder':'direccion'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
             'class':'form-control',
            'placeholder':'contraseña'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
             'class':'form-control',
            'placeholder':'Repita contraseña'
        }
    ))
    class Meta:
        model = User
        fields = ['rut','nombre','correo','telefono','direccion','password1','password2']

 
