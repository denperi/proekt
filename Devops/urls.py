from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demand/', views.demand, name='demand'),
    path('geography/', views.geography, name='geography'),
    path('skills/', views.skills, name='skills'),
    path('last_vacancies/', views.last_vacancies, name='last_vacancies'),
]
