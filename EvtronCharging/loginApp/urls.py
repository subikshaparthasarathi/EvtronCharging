from django.urls import path
from . import views
urlpatterns = [
    path('loginApp/host.html', views.login, name='signin'),
    path('loginApp/host.html', views.login, name='signup')
   
]
