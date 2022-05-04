from django.urls import path
from .views import charging_det
urlpatterns = [
    path('charging/', charging_det)
    
]