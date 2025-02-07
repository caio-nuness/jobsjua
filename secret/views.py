from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_enterprise, logout as logout_platform
from django.contrib.auth.decorators import login_required
from jobs.forms import EnterpriseForm, LoginForm

from secret.forms import VacancieForm
from jobs.models import Enterprise, Vacancie


def login(request):

  if request.method == "GET":

    form = LoginForm()
    context = {'form': form}

    return render(request, template_name="login.html", context=context)
  
  else:

    new_email = request.POST.get('email')
    new_password = request.POST.get('password')

    # o email informado está sendo validado - vendo se existe mesmo na base de dados
    email = Enterprise.objects.filter(email=new_email).first()

    if email: # se ele existir faz isso aqui ate aqui funciona normal

      # autentica o usuario com os dados informados
      enterprise = authenticate(email=new_email, password=new_password)

      # se a autenticação não der None e a empresa estiver Ativa
      if enterprise is not None and enterprise.is_active:
        login_enterprise(request, enterprise)
        return redirect('platform')
      
      else: 
        return HttpResponse(f'ERROR: Resultado da autenticação:  {enterprise}')

    else:
      return HttpResponse('nao existe na base de dados "email"')
   
def register(request):

  if request.method == "GET":

    user = request.user
    
    form = EnterpriseForm()

    context = {
      'form':form,
      'user': user,
    }

    return render(request, "register_enterprise.html", context=context )

  else:
      cnpj = request.POST.get('cnpj')
      username = request.POST.get('username')
      sector = request.POST.get('sector')
      email = request.POST.get('email')
      phone = request.POST.get('phone')
      whatsapp = request.POST.get('whatsapp')
      is_hiring = request.POST.get('is_hiring')
      password = request.POST.get('password')
    
    # ADICIONANDO OS DADOS DO FORM NO MODEL USER MODIFICADO "Enterprise"
      new_enterprise = Enterprise(
        cnpj=cnpj,
        username=username,
        sector=sector,
        email=email,
        phone=phone,
        whatsapp=whatsapp,
        is_hiring=is_hiring,
        password=password
      )

      #VERIFICANDO SE O CNPJ INFORMADO JÁ EXISTE NA BASE DE DADOS
      cnpj_is_valid = Enterprise.objects.filter(cnpj=cnpj).first()

      if cnpj_is_valid: # SE O RETORNO FOR TRUE - NÃO CONCLUI O CADASTRO
        return HttpResponse('CNPJ ja existe na base de dados, tente novamente!')
      
      else: # SE O RETORN FOR FALSE - CRIA O CADASTRO DA EMPRESA - COM SUCESSO
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
        # FALTA IMPLEMENTAR REDIRECIONAMENTO PARA A PAGINA DE LOGIN SE O CADASTRO FOR CONCLUIDO
    
@login_required(login_url='login') #  redireciona user não autenticado
def platform(request): # ESSA VIEW SO PODE SER ACESSADA SE O USUARIO ESTIVER LOGADO/AUTENTICADO


    # PEGA A EMPRESA QUE ESTÁ LOGADA
    enterprise_loggedin = request.user

    # MOSTRAR AS VAGAS REFERENTES A EMPRESA QUE ESTÁ LOGADA
    print(enterprise_loggedin)

    # BUSCA A VAGA EM QUE A EMPRESA QUE CADASTROU == A EMPRESA QUE ESTÁ LOGADA
    company_vacancie = Vacancie.objects.filter(enterprise=enterprise_loggedin)

   
    print(company_vacancie)

   


    # SIRVO A VAGA DA MANEIRA QUE EU PREFERI
    context = {
      "company_vacancie": company_vacancie,
    }


    
    return render(request, template_name='platform.html', context=context)

@login_required(login_url='login')
def secret_one_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)

  context = { 'vacancie': vacancie }

  return render(request, template_name="secret_one_vacancie.html", context=context)

@login_required(login_url='login')
def new_vacancie(request):

  # Empresa que está logada - "Mais Que Bom"
  enterprise_on = request.user

  form  = VacancieForm()

  context = {
    'enterprise_on': enterprise_on,
    'form': form,
  }

  return render(request, template_name="register_vacancie.html", context=context)

@login_required(login_url='login')
def logout(request):
  logout_platform(request)
  return redirect("login")

