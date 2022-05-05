from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import charging_mastertable,charging_transactiontable
from .serializers import charging_mastertableSerializer,charging_transactiontableSerializer

class charging(APIView):

    def get(self, request):
        chargingdata = charging_transactiontable.objects.all()
        serializer = charging_transactiontableSerializer(chargingdata, many = True)
        return Response(serializer.data)

    def post(self):
        pass



