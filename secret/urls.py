
from django.urls import path, include
from . import views



urlpatterns = [
    
    path('login/',views.login , name='login'),
    path('register/',  views.register, name='register'),
    path('logout/', views.logout, name="logout"),
    path('platform/', views.platform, name='platform'),
    path('platform/secret_one_vacancie/<int:id>/',views.secret_one_vacancie, name='secret_one_vacancie'),
    path('platform/new_vacancie/',views.new_vacancie, name="new_vacancie")

]