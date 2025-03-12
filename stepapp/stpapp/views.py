from django.shortcuts import render, get_object_or_404, redirect
from .forms import VacancyForm
from .models import Category, Job, Vacancy

# Главная страница
def home(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()
    context = {
        "categories": categories,
        "jobs": jobs
    }
    return render(request, "index.html", context)

# Страница "О компании"
def about(request):
    return render(request, "about.html")

# Страница регистрации (контактов)
def contact(request):
    return render(request, "registr.html")

# Список вакансий
def vacancy_list(request):
    vacancies = Vacancy.objects.all()   
    return render(request, "vacancy_list.html", {"vacancies": vacancies})

# Детали вакансии
def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    return render(request, "vacancy_detail.html", {"vacancy": vacancy})

# Создание вакансии
def vacancy_create(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vacancy_list")
    else:
        form = VacancyForm()
    return render(request, "vacancy_form.html", {"form": form})

# Редактирование вакансии (исправлено имя ссылки)
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect("vacancy_detail", pk=vacancy.pk)  # Исправлено
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, "vacancy_form.html", {"form": form})

# Удаление вакансии
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        vacancy.delete()
        return redirect("vacancy_list")
    return render(request, "vacancy_confirm_delete.html", {"vacancy": vacancy})
