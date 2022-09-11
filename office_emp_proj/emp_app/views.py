from datetime import datetime
from multiprocessing import context
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Employee, Role, Department

# Create your views here.


def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    print(context)

    return render(request,'view_all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        print("post")

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']

        new_emp = Employee(first_name=first_name, last_name = last_name, salary = salary, bonus = bonus, phone = phone, dept_id = dept, role_id=role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")


    elif request.method == "GET":
        print("get")

        return render(request,'add_emp.html')

    else:
        return HttpResponse("Error occured")


def remove_emp(request, emp_id=0):

    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed")
        except:
            return HttpResponse("Enter valid emp id")

    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'remove_emp.html', context)


def filter_emp(request):
    return render(request,'filter_emp.html')
