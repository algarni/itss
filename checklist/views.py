from django.shortcuts import render

from checklist.models import ListTemplate


def home(request):
    list_templates = ListTemplate.objects.all()
    return render(request, 'checklist/home.html', {'list_templates': list_templates})


def create(request):
    return render(request, 'checklist/create_checklist.html')
