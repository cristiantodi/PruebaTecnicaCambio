from django.contrib import admin
from .models import UsuarioRedactor, Articulo, Suscripcion

# Register your models here.

@admin.register(UsuarioRedactor)
class UsuarioRedactorAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'correo', 'activo']
    list_filter = ['activo']
    search_fields = ['nombre_completo', 'correo']
    ordering = ['nombre_completo']

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_publicacion', 'get_estado_display', 'autor']
    list_filter = ['estado', 'fecha_publicacion']
    search_fields = ['titulo', 'autor__nombre_completo']
    ordering = ['-fecha_publicacion']

    def get_estado_display(self, obj):
        return obj.get_estado_display()
    get_estado_display.short_description = 'Estado'

@admin.register(Suscripcion)
class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'get_tipo_display', 'fecha_inicio', 'fecha_fin']
    list_filter = ['tipo', 'fecha_inicio']
    ordering = ['-fecha_inicio']

    def get_tipo_display(self, obj):
        return obj.get_tipo_display()
    get_tipo_display.short_description = 'Tipo'