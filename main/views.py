from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.all()     # Model: read all rows
    return render(request, 'main/home.html', {
        'students': students,            # View: hand data to the template
        'total': students.count(),
    })
