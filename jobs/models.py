from django.db import models
   
class Enterprise(models.Model):

  HIRING_CHOICES = (
    (True, "Sim"),
    (False, "Não"),
  )

  cnpj = models.CharField(max_length=14, null=False, blank=False, verbose_name="CNPJ")
  social_name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Razão social")
  sector = models.CharField(max_length=200, verbose_name="Setor")
  email = models.EmailField(blank=False, null=False, verbose_name="Email")
  phone = models.CharField(max_length=11, blank=False, null=False, verbose_name="Telefone")
  whatsapp = models.CharField(max_length=11, blank=False, null=True, verbose_name="WhatsApp")
  is_hiring = models.BooleanField(choices=HIRING_CHOICES, verbose_name="Está contratando")
  password = models.CharField(max_length=200, verbose_name="Senha")
  re_password = models.CharField(max_length=200, verbose_name="Confirme senha")

  def __str__(self):
    return self.social_name

class Vacancie(models.Model):

  TYPE_MODALITY = (
    ("CLT - Efetivo",     'CLT - Efetivo'),
    ("CLT - Ferista",     'CLT - Ferista'),
    ("CLT - Contrato",    'CLT - Contrato'),
    ("AVULSO - Diaria",   'AVULSO - Diaria'),
    ("AVULSO - Semanal",  'AVULSO - Semanal'),
    ("AVULSO - Quinzena", 'AVULSO - Quinzena'),
    ("CNPJ - Prestação de serviço",  'CNPJ - Prestação de serviço'),
  )

  TYPE_JOURNEY = (
    ("Escala - 5x1",      'Escala - 5x1'),
    ("Escala - 5x2",      'Escala - 5x2'),
    ("Escala - 6x1",      'Escala - 6x1'),
    ("Escala - 12x36",    'Escala - 12x36'),
    ("Escala - 18x36",    'Escala - 18x36'),
    ("Diaria - 1 Dia",    'Diaria - 1 Dia'),
    ("Diaria - 7 Dias",   'Diaria - 7 Dias'),
    ("Diaria - 15 Dias",  'Diaria - 15 Dias'),
  )

  TYPE_STATE = (
    (True,'Vaga aberta'),
    (False,'Vaga fechada'),
  )

  title = models.CharField(max_length=200, blank=False, null=False, verbose_name="Titulo")

  enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, verbose_name="Empresa")

  email = models.CharField(max_length=200, blank=False, null=False, verbose_name="Email")

  whatsapp = models.CharField(max_length=200, blank=False, null=False, verbose_name="WhatsApp")

  wage = models.FloatField(max_length=200, blank=False, null=False, verbose_name="Salário")

  modality = models.CharField(choices=TYPE_MODALITY, verbose_name="Modalidade", max_length=200)

  weekly_journey = models.CharField(choices=TYPE_JOURNEY, verbose_name="Jornada", max_length=200)

  work_shift = models.CharField(max_length=200, blank=False, null=False, verbose_name="Turno")

  state = models.BooleanField( choices=TYPE_STATE, default=True , verbose_name="Estado",  )

  description = models.TextField(max_length=2000, blank=False, null=False, verbose_name="Descrição")

  create_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title

class User(models.Model):
  name = models.CharField(max_length=100, blank=False, null=False, )
  email_for_hiring = models.EmailField(max_length=200)
  phone = models.CharField(max_length=11, blank=False, null=False)
  whatsapp = models.CharField(max_length=11, blank=False, null=False)
  password = models.CharField(max_length=200)
  re_password = models.CharField(max_length=200)
  vacancies = models.ForeignKey(Vacancie, verbose_name="Vagas",default="", on_delete=models.CASCADE)

  def __str__(self):
    return self.name