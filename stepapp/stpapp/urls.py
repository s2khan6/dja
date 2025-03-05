from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home_page'),
	path('about/', views.about, name='about_page'),
	path('contact/', views.contact, name='content_page'),
	path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
	path('vacancy/new/', views.vacancy_create, name='vacancy_detail'),
	path('vacancy/<int:pk>/edit/', views.vacancy_update, name='vacancy_update'),
	path('vacancy/<int:pk>/delete/', views.vacancy_delete, name='vacancy_delete'),
	
]