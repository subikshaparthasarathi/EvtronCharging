from django.urls import path
from .views import charging
urlpatterns = [
    path('',charging.as_view()),
    
]