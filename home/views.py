from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'  # specificam calea catre pagina html din folder-ul template

