from rest_framework import serializers
from host.models import Useractivity_table,Usermaster_table

class Usermaster_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usermaster_table
        fields=('email', 'pass1', 'status', 'verified')

class Useractivity_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Useractivity_table
        fields=('email', 'login_time', 'logout_time')