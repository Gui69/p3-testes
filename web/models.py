from pyexpat import model
from django.db import models


COMPONENTES_CURRICULARES = (
    ('LP', 'LÍNGUA PORTUGUESA'),
    ('MA', 'MATEMÁTICA'),
    ('CI', 'CIÊNCIAS DA NATUREZA'),
    ('HI', 'HISTÓRIA'),
    ('GE', 'GEOGRAFIA'),
    ('AR', 'ARTES'),
    ('EF', 'EDUCAÇÃO FÍSICA'),
    ('ER', 'ENSINO RELIGIOSO'),
)

# Create your models here.

class Base(models.Model):
    criacao = models.DateField("Data de criação", auto_now_add=True)
    modificado = models.DateField("Data de atualização", auto_now= True)
    ativo = models.BooleanField("Ativo?", default= True)
    
    class Meta:
        abstract = True
    
class Professor(Base):
    email = models.CharField('E-mail', max_length=100, null= False, blank= False)
    senha = models.EmailField('Senha', null=False, blank= False, unique= True)
    

class PerfilProfessor(Professor):
   
    GENERO = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO'),
    )
    
    ESCOLARIDADE = (
        ('1', 'MAGISTÉRIO'),
        ('2', 'SUPERIOR COMPLETO'),
        ('3', 'MESTRADO'),
        ('4', 'DOUTORADO'),
    )
    
    ETAPAS_DE_ENSINO = (
        ('1', 'EDUCAÇÃO INFANTIL'),
        ('2', 'ENSINO FUNDAMENTAL - ANOS INICIAIS'),
        ('3', 'ENSINO FUNDAMENTAL - ANOS FINAIS'),
        ('4', 'ENSINO MÉDIO'),
    )
    nome = models.CharField('Nome', max_length= 255, null= False, blank= False)
    numero_telefone = models.CharField('Telefone', max_length= 11)
    data_nascimento = models.DateField('Data de Nascimento')
    genero = models.CharField('Gênero', max_length= 20, choices= GENERO)
    ocupacao_atual = models.CharField('Ocupação Atual', max_length= 100)
    escolaridade = models.CharField('Escolaridade', max_length= 20, choices= ESCOLARIDADE)
    etapa_de_ensino = models.CharField('Etapas de Ensino', max_length= 50, choices= ETAPAS_DE_ENSINO)
    componente_curricular = models.CharField('Componente Curricular', max_length= 50, choices= COMPONENTES_CURRICULARES)
    
    
class PlanoDeAula(Base):
    
    TURNO = (
        ('1', 'MANHÃ'),
        ('2', 'TARDE'),
        ('3', 'NOITE'),
    )
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    titulo = models.CharField('Título da Aula', max_length= 255, null= False, blank= False)
    componente_curricular = models.CharField('Componente Curricular', max_length= 20, choices= COMPONENTES_CURRICULARES)
    ano_serie = models.CharField('Ano/Série', max_length= 20)
    turma = models.CharField('Turma', max_length= 50, null= False, blank= False)
    turno = models.CharField('Turno', max_length= 20, choices= TURNO)
    duracao = models.CharField('Hora aula', max_length= 2, null= False, blank= False)
    anexos = models.FileField('Anexos')
    referencias = models.CharField('Referências', max_length= 1000)
    