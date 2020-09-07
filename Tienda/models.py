from django.db import models

# Create your models here.
class Docente(models.Model):
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     edad = models.IntegerField(default=10)
     email = models.EmailField(default =  "ii@itsgg.edu.ec")
     sexo = models.CharField(max_length=1)
     estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
     user = models.CharField(max_length=15)
     user_mod = models.CharField(max_length=15)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     class Meta:
         db_table="tr_docente"
         verbose_name = "docente"
         verbose_name_plural = "docentes"

     def __str__(self):
         return self.apellido + ' ' + self.nombre


#
# class Project(models.Model):
#    tittle = models.CharField(length=200)
#    description = models.TextField()
#    user = models.CharField(length=20)
#    user_mod = models.CharField(length=20)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
#
#
class Estudiante(models.Model):
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     edad = models.IntegerField(default=10)
     sexo = models.CharField(max_length=1)
     estado = models.IntegerField(default=1) # 1 es activo y 2 es eliminado
     user = models.CharField(max_length=20)
     user_mod = models.CharField(max_length=20)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     class Meta:
        db_table="tr_estudiante"
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

     def __str__(self):
         return self.apellido


class Letras(models.Model):
    letra1=models.CharField(max_length=1)
    letra2=models.CharField(max_length=1)
    letra3 = models.CharField(max_length=1)
    letra4 = models.CharField(max_length=1)
    letra5 = models.CharField(max_length=1)









