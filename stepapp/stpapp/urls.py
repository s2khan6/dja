from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index_page'),
    path('about/', views.about, name='about_page'),
    path('contact/', views.contact, name='registr_page'),
    path('vacancy/', views.vacancy_list, name='vacancy_list'),  # Добавлено
    path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancy/create/', views.vacancy_create, name='vacancy_create'),
    path('vacancy/<int:pk>/edit/', views.vacancy_update, name='vacancy_update'),
    path('vacancy/<int:pk>/delete/', views.vacancy_delete, name='vacancy_delete'),

]
	