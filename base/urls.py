from django.urls import path
from .views import HomeView, AboutP3View, ClassPlanView, ClassReportsView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutP3View.as_view(), name = 'about'),
    path('class_plan/', ClassPlanView.as_view(), name='class_plan'), 
    path('class/', ClassReportsView.as_view(), name="class"),   
    
    path('login/', LoginView.as_view(), name = "login"), 
]