from urllib import request

from django.shortcuts import redirect, render

from.models import *

from .forms import EmployeeForm

# Create your views here.

def home(request):
    employees = Employees.objects.all()
    return render(request, 'base.html', {'employees': employees})

def forms(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }

        # Code to save your Employee object to the database goes here...

    return render(request, 'forms.html',context)

def edit(request, id=id):
    employees = Employees.objects.get(id=id)
    form = EmployeeForm(instance=employees)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employees)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'forms.html', context)

def delete(request, id):
    employee = Employees.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('/')
    context = {
        'item': employee
    }
    return render(request, 'delete.html', context)