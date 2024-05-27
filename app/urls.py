from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name='clientes'),
    path('faq/', views.faq, name='faq'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('precios/', views.precios, name='precios'),
    #TEST PARA CLIENTES APP
    path('registro/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]
