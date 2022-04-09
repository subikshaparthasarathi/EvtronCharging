from django.urls import path
from . import views
urlpatterns = [
    path('', views.signin, name='host'),
    path('franchise/', views.signin, name='franchise'),
    path('admin/', views.signin, name='admin'),
]
