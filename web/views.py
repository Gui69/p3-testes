from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "web/pages/home.html"

class SobreP3View(TemplateView):
    template_name = "web/pages/sobrep3.html"

class LoginView(TemplateView):
    template_name = "web/pages/login.html"
    
class PerfilView(TemplateView):
    template_name = "web/pages/perfil.html"
    
class PlanejamentoView(TemplateView):
    template_name = "web/pages/planejamento.html"
