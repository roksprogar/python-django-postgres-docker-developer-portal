from django.shortcuts import render
from .models import Project

# This is a list of discionaries.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project-list.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/project-single.html', {'project': projectObj})
