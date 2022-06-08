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
    
class PlanosView(TemplateView):
    template_name = "web/pages/planos.html"
    
class CriarPlanoView(TemplateView):
    template_name = "web/pages/criar-plano.html"

class RelatoriosView(TemplateView):
    template_name = "web/pages/relatorio_turma.html"    
