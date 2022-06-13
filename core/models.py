from tabnanny import verbose
from django.db import models



# Create your models here.
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True, verbose_name="Id del Cliente")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    rut = models.CharField(max_length=10, verbose_name="rut")
    direccion = models.CharField(max_length=30, verbose_name="direccion")
    telefono = models.CharField(max_length=15, verbose_name="telefono")

    def __str__(self):
        return self.idCliente
        
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id del Producto')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    precio = models.IntegerField( verbose_name='Precio') 
    descripcion = models.CharField(max_length=40, verbose_name = 'Descripcion')
    imagen = models.ImageField(upload_to='productos')

    def __str__(self):
        return self.idProducto

    
# class Categoria(models.Model):
#     idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
#     nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

#     def __str__(self):
#         return self.nombreCategoria


# class Vehiculo(models.Model):
#     patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
#     marca= models.CharField(max_length=20, verbose_name='Marca')
#     modelo=models.CharField(max_length=20, verbose_name='Modelo')
#     categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

#     def __str__(self):
#         return self.patente