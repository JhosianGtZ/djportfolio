from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", {'projects': projects})


def detail(request, project_id):
    project= get_object_or_404(Project, pk=project_id)
    return render(request, "detail.html", {'project': project})