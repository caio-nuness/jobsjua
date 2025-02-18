import requests
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from django.contrib.auth import login as login_enterprise, authenticate, logout as logout_platform
from django.contrib.auth.decorators import login_required 
from secret.forms import VacancieForm
from jobs.forms import EnterpriseForm, LoginForm
from secret.forms import RecoveryPasswordForm
from jobs.models import Enterprise, Vacancie
from django.core.paginator import Paginator 
from django.contrib.auth.hashers import make_password


def login(request):

  if request.method == "GET":

    form = LoginForm()
    context = {'form': form}

    return render(request, template_name="login.html", context=context)
  
  else:

    new_email = request.POST.get('email')
    new_password = request.POST.get('password')

    email = Enterprise.objects.filter(email=new_email).first()

    if email:

      enterprise = authenticate(email=new_email, password=new_password)

      if enterprise is not None and enterprise.is_active:
        login_enterprise(request, enterprise)
        return redirect('platform')
      
      else: 
        return HttpResponse(f'ERROR: Resultado da autenticação:  {enterprise}')

    else:
      return HttpResponse('nao existe na base de dados "email"')

def register(request):
  
  """
    ESSA FUNÇÃO REGISTRA UM USUARIO APENAS SE
    - O CNPJ INFORMADO EXISTIR
    - O CNPJ INFORMADO NÃO EXISTA NA BASE DE DADOS 
  """
   
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

      try:
        response = requests.get(f'https://api.cnpjs.dev/v1/{cnpj}')
        data = response.json()
        cnpj_api = data['cnpj']

        # SE O CNPJ EXISTIR NA BASE DE DADOS -  NÃO FOR NULL
        if cnpj_api == cnpj:

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
          
          else: # SE O RETURN FOR FALSE - CRIA O CADASTRO DA EMPRESA - COM SUCESSO
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
            
            return redirect('login')
          
      except:
        print("Ocorreu um erro na requisição")
        
        return HttpResponse("Ocorreu  erro na Requisição")

# REFERENTE A RECUPERAÇÃO DE SENHA
def recovery_password(request):

  if request.method == "GET":

    form = RecoveryPasswordForm()
    context = {"form": form}
    return render(request, template_name="recovery_password.html", context=context)

  else:

    # captura de email informado
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    
    print(email, password, password2)
    # validação de email informado
    try:
      enterprise_register = Enterprise.objects.get(email=email)
      print(enterprise_register)
      
    
      if password == password2:
        
          # criptografando senha
          password = make_password(password) 
          password2 = make_password(password)

          print(f'Senha:{password} - confirm: {password2}')

          enterprise_register.password = password

          enterprise_register.save()

          return HttpResponse("Senha atualizada com sucesso!!")
      else: 
          
          return HttpResponse('As senhas não são iguais!!')

      

      return redirect('change_password')
        
    except:
      return HttpResponse('Nenhuma empresa registrada com esse email, tente novamente!')
    

    

    

# VER TODAS AS VAGAS
@login_required(login_url='login')
def platform(request): 

    enterprise_loggedin = request.user
    
    # BUSCA A VAGA EM QUE A EMPRESA QUE CADASTROU == A EMPRESA QUE ESTÁ LOGADA
    company_vacancie = Vacancie.objects.filter(enterprise=enterprise_loggedin)

    vacancie_paginator = Paginator(company_vacancie, 3)
    page_num = request.GET.get('page')

    page = vacancie_paginator.get_page(page_num)


    context = {
      "company_vacancie": company_vacancie,
      "page": page
    }

    return render(request, template_name='platform.html', context=context)

@login_required(login_url='login')
def secret_one_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)

  context = { 'vacancie': vacancie }

  return render(request, template_name="secret_one_vacancie.html", context=context)

@login_required(login_url='login')
def new_vacancie(request):

  if request.method == "GET":

    enterprise = Enterprise.objects.get(username=request.user)

    form  = VacancieForm()

    context = {
      'form': form,
      'enterprise':enterprise
    }

    return render(request, template_name="register_vacancie.html", context=context)
  
  else:
    title = request.POST.get('title')
    enterprise = Enterprise.objects.get(username=request.user) # PEGA A EMPRESA LOGADA COMO PADRÃO
    email = request.POST.get('email')
    whatsapp = request.POST.get('whatsapp')
    wage = request.POST.get('wage')
    modality = request.POST.get('modality')
    weekly_journey = request.POST.get('weekly_journey')
    work_shift = request.POST.get('work_shift')
    state = request.POST.get('state')
    description = request.POST.get('description')

    # ATRELA OS DADOS COLETADOS AO MODEL VACANCIE
    new_vacancie = Vacancie.objects.create(
      title=title,
      enterprise=enterprise,
      email=email,
      whatsapp=whatsapp,
      wage=wage,
      modality=modality,
      weekly_journey=weekly_journey,
      work_shift=work_shift,
      state=state,
      description=description
    )
    
    new_vacancie.save()

    return redirect('platform')

@login_required(login_url='login')
def edit_vacancie(request, id):

  vacancie = Vacancie.objects.get(id=id)
  form = VacancieForm(instance=vacancie)

  if request.method == "GET":
    context = { 'vacancie': vacancie,'form': form }
    return render(request, template_name='edit_vacancie.html', context=context)

  else:
    title = request.POST.get('title')
    enterprise = Enterprise.objects.get(username=request.user)  # PEGA A EMPRESA LOGADA COMO PADRÃO
    email = request.POST.get('email')
    whatsapp = request.POST.get('whatsapp')
    wage = request.POST.get('wage')
    modality = request.POST.get('modality')
    weekly_journey = request.POST.get('weekly_journey')
    work_shift = request.POST.get('work_shift')
    state = request.POST.get('state')
    description = request.POST.get('description')

    vacancie.title = title
    vacancie.enterprise = enterprise
    vacancie.email = email
    vacancie.whatsapp = whatsapp
    vacancie.wage = wage
    vacancie.modality = modality
    vacancie.weekly_journey = weekly_journey
    vacancie.work_shift = work_shift
    vacancie.state = state
    vacancie.description = description

    vacancie.save()

    return  redirect(f'secret_one_vacancie', id=id)

@login_required(login_url='login')
def delete_vacancie(request, id):
  vacancie = Vacancie.objects.get(id=id)
  vacancie.delete()
  return redirect('platform')

@login_required(login_url='login')
def logout(request):
  logout_platform(request)
  return redirect("login")
