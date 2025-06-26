from django.db import models

# Create your models here.

class UsuarioRedactor(models.Model):
    nombre_completo = models.CharField(max_length=255)
    correo      = models.EmailField(unique=True)
    activo      = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_completo

class Articulo(models.Model):
    BORRADOR    = 'borrador'
    PUBLICADO   = 'publicado'
    ESTADO_CHOICES = [(BORRADOR, 'Borrador'), (PUBLICADO, 'Publicado')]
    titulo      = models.CharField(max_length=255)
    contenido   = models.TextField()
    fecha_publicacion = models.DateField()
    estado      = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    autor       = models.ForeignKey(UsuarioRedactor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Suscripcion(models.Model):
    GRATUITA    = 'gratuita'
    PAGO        = 'pago'
    TIPO_CHOICES = [(GRATUITA, 'Gratuita'), (PAGO, 'Pago')]
    usuario     = models.CharField(max_length=255)
    tipo        = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin   = models.DateField()


    def __str__(self):
        return self.usuario