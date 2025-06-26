import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from appPrueba.models import Articulo

class Command(BaseCommand):
    help = 'Exporta artículos publicados a un archivo CSV'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fecha',
            type=str,
            help='Fecha desde la cual exportar (formato YYYY-MM-DD)'
        )

    def handle(self, *args, **options):
        fecha = options['fecha']
        articulos = Articulo.objects.filter(estado='publicado')

        if fecha:
            try:
                fecha_obj = datetime.strptime(fecha, '%Y-%m-%d').date()
                articulos = articulos.filter(fecha_publicacion__gte=fecha_obj)
            except ValueError:
                self.stderr.write("Formato de fecha inválido. Usa YYYY-MM-DD.")
                return

        articulos = articulos.order_by('-fecha_publicacion')

        with open('articulos_exportados.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'titulo', 'fecha_publicacion', 'estado', 'autor_id'])
            for articulo in articulos:
                writer.writerow([
                    articulo.id,
                    articulo.titulo,
                    articulo.fecha_publicacion,
                    articulo.estado,
                    articulo.autor_id
                ])

        self.stdout.write(self.style.SUCCESS(f'Se exportaron {articulos.count()} artículos a "articulos_exportados.csv"'))
