from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastroDespesa.as_view(), name='despesas'),
    path('add', views.AddDespesa.as_view(), name='cadastrar')
]
