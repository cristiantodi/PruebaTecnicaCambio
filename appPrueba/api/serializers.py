from rest_framework import serializers
from appPrueba.models import Articulo, Suscripcion

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        exclude = []

class SuscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = '__all__'

    def validate(self, data):
        user = data['usuario']
        hoy = data['fecha_inicio']
        existe = Suscripcion.objects.filter(
            usuario=user,
            fecha_inicio__lte=hoy,
            fecha_fin__gte=hoy
        ).exists()
        if existe:
            raise serializers.ValidationError("Ya existe una suscripción activa.")
        return data
