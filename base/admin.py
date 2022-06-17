from django.contrib import admin
from .models import Habilidade

# Register your models here.
class HabilidadeAdmin(admin.ModelAdmin):
    fields = ['descricao', 'ativo']
    list_display = ('id','descricao', 'criacao', 'modificado')

    list_filter = ['criacao']
    search_fields = ['descricao'] 

admin.site.register(Habilidade, HabilidadeAdmin) 
