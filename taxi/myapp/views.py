from django.shortcuts import render
from . models import User

# Create your views here.
def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def blog(request):
	return render(request,'blog.html')

def car(request):
	return render(request,'car.html')

def contact(request):
	return render(request,'contact.html')

def signup(request):
	if request.method=="POST":
		if request.POST['password']==request.POST['cpassword']:
			User.objects.create(
				fname=request.POST['fname'],
				lname=request.POST['lname'],
				email=request.POST['email'],
				mobile=request.POST['mobile'],
				address=request.POST['address'],
				password=request.POST['password'],
				profile_pic=request.FILES['profile_pic']
				)
			msg="User Signup Successfully"
			return render(request,'signup.html',{'msg':msg})
		else:
			msg="Password & Confirm Password Does Not Matched"
			return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		user=User.objects.get(email=request.POST['email'])
		if request.POST['password']==request.POST['password']:
			request.session['fname']=user.fname
			request.session['email']=user.email
			request.session['profile_pic']=user.profile_pic.url
			return render(request,'index.html')
		else:
			msg="Incorrect Password"
			return render(request,'login.html')
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')
