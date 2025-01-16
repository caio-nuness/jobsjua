from django import forms
from .models import Enterprise, User, Vacancie

class EnterpriseForm(forms.ModelForm):
  
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
  
  social_name = forms.CharField(
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
        'placeholder': 'Digite sua senha novamente'
      }
    )
  )
  
  re_password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-green-500 sm:text-sm/6',
        'placeholder': 'Digite sua senha novamente'
      }
    )
  )

  class Meta:
    model = Enterprise
    fields = ("__all__")

class UserForm(forms.ModelForm):

  password = forms.CharField(max_length=200, widget=forms.PasswordInput)
  re_password = forms.CharField(max_length=200, widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ("__all__")
  
class VacancieForm(forms.ModelForm):

  class Meta:
    model = Vacancie
    fields = ("__all__")

