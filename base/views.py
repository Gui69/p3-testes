from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "base/pages/home.html"

class AboutP3View(TemplateView):
    template_name = "base/pages/about_p3.html"
    
class ClassPlanView(TemplateView):
    template_name = "base/pages/class_plan.html"

class ClassReportsView(TemplateView):
    template_name = "base/pages/class.html"   
    
class LoginView(TemplateView):
    template_name = "base/components/modal.html" 