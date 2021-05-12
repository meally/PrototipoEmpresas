from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Producto
import io, csv


def get_productos(request):
    productos = Producto.objects.order_by('fecha_vencimiento')
    context = {
        'productos': productos,
    }
    return render(request, 'employee/productos.html', context)

class EmployeeUploadView(View):

    def get(self, request):
        template_name = 'employee/importemployee.html'
        return render(request, template_name)

    def post(self, request):
        paramFile = io.TextIOWrapper(request.FILES['productfile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            Producto(
                nombre=row['nombre'],
                cantidad=row['cantidad'],
                fecha_vencimiento = row['fecha_vencimiento'],
                #FORMATO DE FECHA: '1970-01-01',
                supermercado=row['supermercado'],
                direccion=row['direccion'],
                recogido=row['recogido'],
            )
            for row in list_of_dict
        ]
        try:
            msg = Producto.objects.bulk_create(objs)
            template_name = 'employee/success.html'
            print('Importado exitosamente')
        except Exception as e:
            print('Error al importar los productos: ', e)
            template_name = 'employee/failure.html'
            returnmsg = {"status_code": 500}

        return render(request, template_name)
