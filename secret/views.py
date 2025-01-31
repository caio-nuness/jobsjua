from django.shortcuts import render, redirect
from django.http import HttpResponse

from jobs.forms import EnterpriseForm
from jobs.models import Enterprise

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password



def login(request):

  if request.method == "GET":

    user = Enterprise.objects.all()
    context = { 'user': user }

    return render(request, template_name="login.html", context=context)
  
  else:

    
   
    email = request.POST.get('email')
    password = request.POST.get('password')

    enterprise = Enterprise.objects.get(email=email, password=password) 
   
    if enterprise:  
      enterprise = authenticate(email=email, password=password)
      return redirect('platform')

    else:
      return HttpResponse('Nao foi possivel autenticar')
     
def register(request):

  if request.method == "GET":
    form = EnterpriseForm()
    context = {'form':form}
    return render(request, "register_enterprise.html", context=context )

  else :
    cnpj = request.POST.get('cnpj')
    username = request.POST.get('username')
    sector = request.POST.get('sector')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    whatsapp = request.POST.get('whatsapp')
    is_hiring = request.POST.get('is_hiring')
    password = request.POST.get('password')
    
# Adicionando os dados do formulario no meu model
    new_enterprise = Enterprise(
      cnpj=cnpj,
      username=username,
      sector=sector,
      email=email,
      phone=phone,
      whatsapp=whatsapp,
      is_hiring=is_hiring,
      password=password,
    )

    cnpj_is_valid = Enterprise.objects.filter(cnpj=cnpj).first()

    #adicionar um set_password
    # vaidação de cnpj existente
    if cnpj_is_valid:
      return HttpResponse('CNPJ ja existe na base de dados, tente novamente!')
    
    else:
      # Modifiquei o create user e deu certo a senha
      new_enterprise = Enterprise.objects.create_user(
        cnpj=cnpj,
        username=username,
        sector=sector,
        email=email,
        phone=phone,
        whatsapp=whatsapp,
        is_hiring=is_hiring,
        password=password,
        is_active=True,
        is_staff=True,
      )

      new_enterprise.save()
      
      return HttpResponse('Empresa cadastrada com sucesso!')
    

@login_required
def platform(request):
  return render(request, template_name='platform.html')