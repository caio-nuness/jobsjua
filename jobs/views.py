from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancie

# VIEWS REFERENTE AS VAGAS 
def view_vacancies(request):

  vacancie = Vacancie.objects.all()

  context = { 'vacancie': vacancie }
  # coloca o id do item que eu cliquei
  return render(request, template_name="view_vacancies.html", context=context)

def view_one_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)

  title =  vacancie.title
  enterprise = vacancie.enterprise
  email = vacancie.email
  whatsapp = vacancie.whatsapp
  wage = vacancie.wage
  modality = vacancie.modality
  jorney = vacancie.weekly_journey
  work_shift = vacancie.work_shift
  state = vacancie.state
  description = vacancie.description
  criado= vacancie.create_at

  print(f'{title} - {enterprise} - {email} - {whatsapp} - {wage} - {modality} - {jorney} - {work_shift} - {state} - {description}- {criado}')
  
  context = {'vacancie': vacancie}

  return render(request, template_name='view_one_vacancie.html', context=context)

def create_job(request):
  return HttpResponse("Criar Vaga")

def update_job(request):
  return HttpResponse("Atualizar Vagas")

def delete_job(request):
  return HttpResponse("Atualizar Vagas")