from django.urls import path
from . import views

urlpatterns = [
    path('view_vacancies/', views.view_vacancies, name='view_vacancies'),
    path('view_one_vacancie/<int:id_vacancie>/', views.view_one_vacancie, name='view_one_vacancie'),
]