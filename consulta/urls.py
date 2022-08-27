from django.urls import path
from . import views

urlpatterns = [
    path('consulta', views.Consulta.as_view(), name='consultar')
]
