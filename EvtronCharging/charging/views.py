from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import charging_mastertable,charging_transactiontable
from .serializers import charging_mastertable, charging_transactiontable

@csrf_exempt
def charging_det(request):
    if request.method == 'GET':
         charging_transactions = charging_transactiontable.objects.all()
         Serializer = charging_transactiontable_serializer(charging_transactions, many=True)
         return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        Serializer = charging_transactiontable_serializer(data = data)

        if Serializer.is_valid():
            Serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)