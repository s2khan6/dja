from django.shortcuts import render
from .models import Category, Job

def home(request):
    categories = Category.objects.all()
    jobs = Job.objects.all()

    context = {
        "categories": categories,
        "jobs": jobs

    }
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")