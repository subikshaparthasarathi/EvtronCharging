from django.contrib import admin
from .models import charging_mastertable,charging_transactiontable

# Register your models here.
admin.site.register(charging_mastertable)
admin.site.register(charging_transactiontable)