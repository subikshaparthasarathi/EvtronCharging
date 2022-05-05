from rest_framework import serializers
from.models import charging_mastertable, charging_transactiontable
from django.db import models, DEFAULT_DB_ALIAS

class charging_mastertableSerializer(serializers.ModelSerializer):
     class Meta:
         model = charging_mastertable
         fields = '__all__'

class charging_transactiontableSerializer(serializers.ModelSerializer):
    class Meta:
        model = charging_transactiontable
        fields = '__all__'
        





