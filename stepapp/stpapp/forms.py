from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy  # Указываем модель (исправлено models → model)
        fields = ['title', 'description', 'company', 'location']  # Исправлено field → fields
