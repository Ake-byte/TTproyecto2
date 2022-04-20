from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    #archivo = models.FileField
    #periodoInicio = 
    #periodoTermino =  
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.nombre