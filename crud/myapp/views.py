from django.shortcuts import render

# Create your views here.
def test(request):
	return render(request,'test.html')

def add_employee(request):
	return render(request,'add-employee.html')