from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
	class Meta:
		models = Vacancy
		field = ['title', 'description', 'company', 'location']