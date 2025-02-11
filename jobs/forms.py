from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Enterprise

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
          'class': 'block w-full rounded-sm  px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe o seu CNPJ....'
        }
    )
  )
  
  username = forms.CharField(
    empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe sua razão social'
        }
    )
  )
  
  sector = forms.CharField(
    empty_value=False,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe o ramo de atividade'
        }
    )
  )

  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
        'placeholder': 'Informe seu melhor email'
      }
    )
  )

  phone = forms.CharField(
    empty_value=False,
    max_length=11,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe seu telefone'
        }
    )
  )

  whatsapp = forms.CharField(
      max_length=11,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe seu whatsapp'
        }
    )
  )

  is_hiring = forms.BooleanField (
    widget=forms.Select(
      choices=HIRING_CHOICES,
      attrs={
         'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Digite sua senha novamente'
      }
    )
  )

  password = forms.CharField(

    widget=forms.PasswordInput(
      attrs={
        'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
        'placeholder': 'Informe a sua senha.'
      }
    )
  )
  
  class Meta(UserCreationForm.Meta):
    model = Enterprise
    fields = UserCreationForm.Meta.fields

  
class LoginForm(forms.ModelForm):

  email = forms.CharField(
    empty_value=False,
    required=True,
      widget=forms.TextInput(
        attrs={
          'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
          'placeholder': 'Informe o email cadastrado...'
        }
    )
  )

  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'block w-full rounded-sm bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-[#588157] sm:text-sm/6',
        'placeholder': 'Informe a sua senha...'
      }
    )
  )

  class Meta:
    model = Enterprise
    fields = ("email", "password")

