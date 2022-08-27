from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Cadastro
from django.http import HttpResponse
from django.views import View


class CadastroDespesa(ListView):
    model = Cadastro
    template_name = 'cadastro/view_cadastro.html'


class AddDespesa(View):
    def get(self, *args, **kwargs):

        ano = self.request.GET.get('ano')
        mes = self.request.GET.get('mes')
        dia = self.request.GET.get('dia')
        tipo = self.request.GET.get('tipo')
        descricao = self.request.GET.get('descricao')
        valor = self.request.GET.get('valor')

        data = dia + '/' + mes + '/' + ano

        print(data, tipo, descricao, valor)

        return redirect('despesas')
