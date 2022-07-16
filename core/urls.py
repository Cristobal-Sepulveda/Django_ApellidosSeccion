from django.urls import path
from .views import index, galeria, carrito, somos, login, contacto,  productos, form_login, form_crear_producto, form_mod_producto, form_del_producto, clientes, form_crear_cliente, form_mod_cliente, form_del_cliente, form_crear_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', index, name='index'),
    path('galeria/', galeria, name='galeria'),
    path("somos/", somos, name="somos"),
    path("contacto/", contacto, name="contacto"),
    path("productos/", productos, name="productos"),
    path("form_crear_producto/", form_crear_producto, name='form_crear_producto'),
    path("form_mod_producto/<id>", form_mod_producto, name='form_mod_producto'),
    path("form_del_producto/<id>", form_del_producto, name='form_del_producto'),
    path("clientes/", clientes, name="clientes"),
    path("form_crear_cliente/", form_crear_cliente, name='form_crear_cliente'),
    path("form_mod_cliente/<id>", form_mod_cliente, name='form_mod_cliente'),
    path("form_del_cliente/<id>", form_del_cliente, name='form_del_cliente'),
    path("form_crear_usuario/", form_crear_usuario, name='form_crear_usuario'),
    path('form_login', form_login, name="form_login"),
    path('login', login, name='login'),
    path('carrito', carrito, name='carrito')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)