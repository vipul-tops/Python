from django.shortcuts import render,redirect
from .models import User,Product
import random
import json
from django.http import JsonResponse,HttpResponse

# Create your views here.
def validate_email(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}
	return JsonResponse(data)

def validate_oldpassword(request):
	oldpassword=request.GET.get('oldpassword')
	user=User.objects.get(email=request.session['email'])
	print(user.fname)
	print(oldpassword)
	data={
		'is_taken':User.objects.filter(password=oldpassword,email=user.email).exists()
	}
	return JsonResponse(data)

def validate_newpassword(request):
	newpassword=request.GET.get('newpassword')
	user=User.objects.get(email=request.session['email'])
	data={
		'is_taken':User.objects.filter(password=newpassword).exists()
	}
	return JsonResponse(data)

def index(request):
	products=list(Product.objects.all())
	random_products = random.sample(products, min(len(products), 3))
	random_product = random.sample(products, min(len(products), 3))
	random_productt = random.sample(products, min(len(products), 3))
	return render(request,'index.html',{'products':products,'random_products':random_products,'random_product':random_product,'random_productt':random_productt})

def seller_index(request):
	products=list(Product.objects.all())
	random_products = random.sample(products, min(len(products), 3))
	random_product = random.sample(products, min(len(products), 3))
	random_productt = random.sample(products, min(len(products), 3))
	return render(request,'seller-index.html',{'products':products,'random_products':random_products,'random_product':random_product,'random_productt':random_productt})

	

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:

				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					usertype=request.POST['usertype'],
					)
				msg="User Signup Are Successsfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password & Confirm Password Does Not MAtched"
				return render(request,'signup.html',{'msg':msg})
	else:		
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="buyer":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['lname']=user.lname
					request.session['profile_pic']=user.profile_pic.url
					#return render(request,'index.html')
					return redirect('index')
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['lname']=user.lname
					request.session['profile_pic']=user.profile_pic.url
					return redirect('seller-index')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['lname']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password==request.POST['oldpassword']:
			if request.POST['newpassword']==request.POST['cnewpassword']:
				user.password=request.POST['newpassword']
				user.save()
				msg="Change Password Successsfully"
				return redirect('logout')
			else:
				msg="New Password & Confirm New password Does Not Matched"
				if user.usertype=="buyer":
					return render(request,'change-password.html',{'msg':msg})
				else:
					return render(request,'seller-change-password.html',{'msg':msg})

		else:
			msg="Password & Old password Does Not Matched"
			if user.usertype=="buyer":
				return render(request,'change-password.html',{'msg':msg})
			else:
				return render(request,'seller-change-password.html',{'msg':msg})
	else:
		if user.usertype=="buyer":
			return render(request,'change-password.html')
		else:
			return render(request,'seller-change-password.html')

def edit_profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		msg="Edit Profile Successsfully"
		request.session['fname']=user.fname
		request.session['lname']=user.lname
		request.session['profile_pic']=user.profile_pic.url 
		if user.usertype=="buyer":
			return render(request,'edit-profile.html',{'user':user,'msg':msg})
		else:
			return render(request,'seller-edit-profile.html',{'user':user,'msg':msg})
	else:	
		if user.usertype=="buyer":
			return render(request,'edit-profile.html',{'user':user})
		else:
			return render(request,'seller-edit-profile.html',{'user':user})

def seller_add_product(request):
	seller=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		Product.objects.create(
			seller=seller,
			product_category=request.POST['product_category'],
			product_name=request.POST['product_name'],
			product_price=request.POST['product_price'],
			product_desc=request.POST['product_desc'],
			product_image=request.FILES['product_image'],
			)
		msg="Product Added Successsfully"
		return render(request,'seller-add-product.html',{'msg':msg})
	else:	
		return render(request,'seller-add-product.html')

def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,'seller-view-product.html',{'products':products})