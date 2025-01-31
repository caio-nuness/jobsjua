from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Enterprise, Unemployed, Vacancie



@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):

  list_display = (
    'id', 'username', 'cnpj', 'sector',
    'email', 'whatsapp', 'is_superuser','password'
  )

  list_display_links = ('username',)

  search_fields = ('cnpj',)

admin.site.register(Unemployed)
admin.site.register(Vacancie)

