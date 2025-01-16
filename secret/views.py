from django.shortcuts import render, redirect
from django.http import HttpResponse
from jobs.forms import EnterpriseForm
from jobs.models import Enterprise
from django.contrib.auth.models import User
from django.contrib import messages

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

    enterprise = Enterprise(
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

    # VARIAVEIS DO BANCO PARA VALIDAÇÃO DE DADOS
    password1 = User.objects.filter(password=password).first()
    password2 = User.objects.filter(password=re_password).first()

    # VALIDAÇÃO SOCIAL NAME JA EXISTENTE
    register_social_name = User.objects.filter(username=social_name).first()
    

    if (password1 != password2):
      return HttpResponse("As senhas não coencidem, tente novamnete")
      

    elif register_social_name:
      return HttpResponse('Razão social já Existe!')

    else:
      register_social_name = User.objects.create(username=social_name, email=email, password=password)
      enterprise.save()
      
      return HttpResponse("Foi criado")
