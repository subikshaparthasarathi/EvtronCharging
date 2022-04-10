from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.signin, name='host_signin'),
    path('', views.signup, name='host_signup'),
    path('activate/<uidb64>/<token>', views.activate, name="activate")
]
