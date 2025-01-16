from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancie

# VIEWS REFERENTE AS VAGAS 
def view_vacancies(request):

  vacancie = Vacancie.objects.all()
  context = { 'vacancie': vacancie }

  return render(request, template_name="view_vacancies.html", context=context)

def view_one_vacancie(request, id_vacancie):

  one_vacancie = Vacancie.objects.all()  
  
  context = {
    'id_vacancie': id_vacancie, 
    'one_vacancie': one_vacancie
  }

  return render(request, template_name='view_one_vacancie.html', context=context)

def create_job(request):
  return HttpResponse("Criar Vaga")

def refresh_jobs(request):
  return HttpResponse("Atualizar Vagas")

def erase_jobs(request):
  return HttpResponse("Apagar Vagas")