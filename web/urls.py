from django.urls import path
from .views import HomeView, LoginView, PerfilView, PlanosView, SobreP3View

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('sobre-P3', SobreP3View.as_view(), name = 'sobreP3'),
    path('login/', LoginView.as_view(), name='login'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('planos/', PlanosView.as_view(), name='planos'),  
]