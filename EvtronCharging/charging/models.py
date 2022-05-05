from django.db import models 
from django.db.models import Model

class charging_mastertable(models.Model):

    Station_ID = models.CharField(null=True, max_length=20)
    Txn_ID = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.Station_ID


class charging_transactiontable(models.Model):
    Station_ID = models.CharField(null=True, max_length=20)
    Local_IP = models.GenericIPAddressField()
    Date_Time = models.DateTimeField(null=True)
    Uptime = models.TimeField(null=True)
    Relay_Status = models.IntegerField(null=True)
    Station_Status = models.CharField(null=True, max_length=50)
    Elapsed_Time = models.TimeField(null=True)
    Amps = models.FloatField(null=True, max_length=50)
    AC_Voltage = models.FloatField(null=True, max_length=50)
    DC_Voltage = models.FloatField(null=True, max_length=50)
    Temperature = models.FloatField(null=True, max_length=50)
    Wattage = models.FloatField(null=True, max_length=50)
    Free_Heap = models.IntegerField(null=True)
    Last_KWH = models.FloatField(null=True, max_length=50)


    def __str__(self):
        return self.Station_ID




