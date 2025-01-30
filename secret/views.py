from django.shortcuts import render, redirect
from django.http import HttpResponse
from jobs.forms import EnterpriseForm

from jobs.models import Enterprise


def login(request):
  return render(request, template_name="login.html")

def register(request):

  if request.method == "GET":
    form = EnterpriseForm()
    context = {'form':form}
    return render(request, "register_enterprise.html", context=context )

  else :
    cnpj = request.POST.get('cnpj')
    social_name = request.POST.get('social_name')
    sector = request.POST.get('sector')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    whatsapp = request.POST.get('whatsapp')
    is_hiring = request.POST.get('is_hiring')
    password = request.POST.get('password')
    re_password = request.POST.get('re_password')

    # Adicionando os dados do formulario no meu model
    new_enterprise = Enterprise(
      cnpj=cnpj,
      social_name=social_name,
      sector=sector,
      email=email,
      phone=phone,
      whatsapp=whatsapp,
      is_hiring=is_hiring,
      password=password,
      re_password=re_password,
    )

    # VARIAVEIS DO BANCO PARA VALIDAÇÃO DE DADOS
    password1 = Enterprise.objects.filter(password=password).first()
    password2 = Enterprise.objects.filter(re_password=re_password).first()
    cnpj_is_valid = Enterprise.objects.filter(cnpj=cnpj).first()  # VALIDAÇÃO  PELO CNPJ JA EXISTENTE
    
    # VALIDAÇÔES
    if (password1 != password2):
      return HttpResponse("As senhas não coencidem, tente novamnete")
      

    elif cnpj_is_valid:
      return HttpResponse('CNPJ já Existe, Tente Novamnete')

    else:
      new_enterprise = Enterprise.objects.create(
        cnpj=cnpj,
        social_name=social_name,
        sector=sector,
        email=email,
        phone=phone,
        whatsapp=whatsapp,
        is_hiring=is_hiring,
        password=password,
        re_password=re_password
      )

      new_enterprise.save()
      
      return HttpResponse("Cadastro criado com sucesso!")
