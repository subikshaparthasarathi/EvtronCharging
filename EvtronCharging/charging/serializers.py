from rest_framework import serializers
from.models import charging_mastertable, charging_transactiontable
from django.db import models, DEFAULT_DB_ALIAS

class charging_mastertable_serializer(serializers.Serializer):
     Station_ID = serializers.CharField()
     Txn_ID = serializers.IntegerField()

class charging_transactiontable_serializer(serializers.Serializer):
    Station_ID = serializers.CharField(max_length=50)
    Local_IP = serializers.IntegerField()
    Date_Time = serializers.DateTimeField()
    Uptime = serializers.TimeField()
    Relay_Status = serializers.IntegerField()
    Station_Status = serializers.CharField(max_length=50)
    Elapsed_Time = serializers.TimeField()
    Amps = serializers.FloatField()
    AC_Voltage = serializers.FloatField()
    DC_Voltage = serializers.FloatField()
    Temperature = serializers.FloatField()
    Wattage = serializers.FloatField()
    Free_Heap = serializers.IntegerField()
    Last_KWH = serializers.FloatField()

    def create(self, Validated_data):
        return charging_transactiontable.objects.create(Validated_data)

    def update(self, instance, Validated_data):
        instance.Station_ID = Validated_data.get('Station_ID', instance.Station_ID)
        instance.Local_IP = Validated_data.get('Local_IP', instance.Local_IP)
        instance.Date_Time = Validated_data.get('Date_Time', instance.Date_Time)
        instance.Uptime = Validated_data.get('Uptime', instance.Uptime)
        instance.Relay_Status = Validated_data.get('Relay_Status', instance.Relay_Status)
        instance.Station_Status = Validated_data.get('Station_Status', instance.Station_Status)
        instance.Elapsed_Time = Validated_data.get('Elapsed_Time', instance.Elapsed_Time)
        instance.Amps = Validated_data.get('Amps', instance.Amps)
        instance.AC_Voltage = Validated_data.get('AC_Voltage', instance.AC_Voltage)
        instance.DC_Voltage = Validated_data.get('DC_Voltage', instance.DC_Voltage)
        instance.Temperature = Validated_data.get('Temperature', instance.Temperature)
        instance.Wattage = Validated_data.get('Wattage', instance.Wattage)
        instance.Free_Heap = Validated_data.get('Free_Heap', instance.Free_Heap)
        instance.Last_KWH = Validated_data.get('Last_KWH', instance.Last_KWH)

        instance.save()
        return instance





