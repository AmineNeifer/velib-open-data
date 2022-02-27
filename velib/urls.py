from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('velib/viz1/', views.viz1, name='viz1'),
    path('velib/viz2/', views.viz2, name='viz2')
]
