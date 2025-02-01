from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Enterprise, Unemployed, Vacancie

class EnterpriseForm(UserCreationForm):
  
  HIRING_CHOICES = (
    (True, "Sim"),
    (False, "Não"),
  )

  cnpj = forms.CharField(
      empty_value=False,
      max_length=14,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe sua razão social'
        }
    )
  )
  
  username = forms.CharField(
    empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe sua razão social'
        }
    )
  )
  
  sector = forms.CharField(
    empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe o ramo de atividade'
        }
    )
  )

  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
        'placeholder': 'Informe seu melhor email'
      }
    )
  )

  phone = forms.CharField(
    empty_value=False,
    max_length=11,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe seu telefone'
        }
    )
  )

  whatsapp = forms.CharField(
      max_length=11,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe seu whatsapp'
        }
    )
  )

  is_hiring = forms.BooleanField (
    widget=forms.Select(
      choices=HIRING_CHOICES,
      attrs={
         'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Digite sua senha novamente'
      }
    )
  )

  password = forms.CharField(

    widget=forms.PasswordInput(
      attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
        'placeholder': 'Informe a sua senha.'
      }
    )
  )
  
  class Meta(UserCreationForm.Meta):
    model = Enterprise
    fields = UserCreationForm.Meta.fields

class UnemployedForm(forms.ModelForm):

  password = forms.CharField(max_length=200, widget=forms.PasswordInput)
  re_password = forms.CharField(max_length=200, widget=forms.PasswordInput)

  class Meta:
    model = Unemployed
    fields = ("__all__")
  
class VacancieForm(forms.ModelForm):

  class Meta:
    model = Vacancie
    fields = ("__all__")

class LoginForm(forms.ModelForm):

  email = forms.CharField(
    empty_value=False,
    required=True,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
          'placeholder': 'Informe o email cadastrado...'
        }
    )
  )

  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
        'placeholder': 'Informe a sua senha...'
      }
    )
  )

  class Meta:
    model = Enterprise
    fields = ("email", "password")

