from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.

def test(request):
	emps = Employee.objects.all()
	return render(request,'test.html',{'emps':emps})

def add_emp(request):
    if request.method=="POST":
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            address=request.POST['address'],
            phone=request.POST['phone'],
            )
        return redirect('test')
    else:
        return render(request,'test.html')

def delete_emp(request,pk):
    emp=Employee.objects.get(pk=pk)
    print(emp)
    emp.delete()

    return redirect('test')
