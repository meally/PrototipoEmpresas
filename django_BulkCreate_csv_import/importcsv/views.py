from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.views import View
from .models import Producto
import io, csv


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
            )
            for row in list_of_dict
        ]
        try:
            msg = Producto.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('Importado exitosamente')
        except Exception as e:
            print('Error al importar los productos: ', e)
            returnmsg = {"status_code": 500}

        return JsonResponse(returnmsg)