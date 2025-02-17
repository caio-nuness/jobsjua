from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancie

from django.core.paginator import Paginator

# VER TODAS AS VAGAS 
def view_vacancies(request):

  # Pegando todos os Objetos
  vacancie = Vacancie.objects.all().reverse()
  print(vacancie)


  # Instancia do paginator
  vacancie_paginator = Paginator(vacancie, 9)

  # Definindo pagina atual
  page_num = request.GET.get('page')

  # Passa o meu objeto listado
  page = vacancie_paginator.get_page(page_num)
  print(page.paginator.num_pages)

  context = { 
    'page': page,
    'vacancie_paginator': vacancie_paginator
  }

  return render(request, template_name="view_vacancies.html", context=context)

# VER APENAS UMA AS VAGA
def view_one_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)
  
  context = {'vacancie': vacancie}

  return render(request, template_name='view_one_vacancie.html', context=context)
