from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
    'id': '1',
    'title': 'Ecommerce Website',
    'description': 'Fully functional ecommerce website'
    },
    {
    'id': '2',
    'title': 'Portfolio Website',
    'description': 'This was a project where I built out my portfolio website'
    },
    {
    'id': '3',
    'title': 'Social Network',
    'description': 'Awesome open source project I am still working on'
    },
]

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for project in projectList:
        if project['id'] == pk:
            projectObj = project
    return render(request, 'projects/single_project.html', {'project': projectObj})
