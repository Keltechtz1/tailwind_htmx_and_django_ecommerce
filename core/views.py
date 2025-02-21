from django.shortcuts import render, redirect
from django.db.models import Q
# Create your views here.

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

 
from .forms import * 

from products.models import *
from order.models import *

def homeView(request):
	products = Product.objects.all()[0:8]


	context = {
			'page_home' : 'home',
			'products' : products
	}
	return  render(request, 'core/index.html', context)


def signUpView(request):
	
	if request.method == "POST":
		form = SignUpForm(request.POST)

		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()

	context = {
			'page' : 'Sign Up',
			'form' : form
	}
	return  render(request, 'core/sign_up.html', context)

def loginView(request):
	if request.user.is_authenticated:
		return redirect('home')
	valuenext = ''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		valuenext= request.POST['next']
		user = auth.authenticate(username=username, password=password)

		if user is not None and valuenext=='':
		  auth.login(request, user)
		  messages.success(request, 'You have successfully logged in.')
		  # if user.profile.role == 'Staff' or user.profile.role == 'Admin':
		  #   return redirect('office:dashboard')
		  return redirect('home')
		
		if user is not None and valuenext!='':
			auth.login(request, user)
			messages.success(request, "You have successfully logged in")
			return redirect(valuenext)

		else:
			messages.error(request, 'Invalid credentials')
			return redirect('login')
	context = {
			'page' : 'login',
			'page_title'  : 'Login ',
	}
	return render(request, 'core/log_in.html', context)




def shopView(request):
	products = Product.objects.all()
	categories = Category.objects.all()

	active_category = request.GET.get('category')

	if active_category : 
		products = Product.objects.filter(category__slug=active_category)

	query = request.GET.get('query')

	if query:
		products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) )


	context = {
			'page' : 'category',
			'products' : products,
			'categories' : categories,
			'active_category' : active_category,
	}
	return  render(request, 'core/shop.html', context)






@login_required 
def myAccount(request):
	orders = Order.objects.filter(user=request.user)
	context ={
		'page' : str(request.user.get_full_name)+' Account',
		'orders' : orders

	}

	return render(request, 'core/my_account.html', context)

@login_required 
def editMyAccount(request):

	if request.method == "POST":

		user = request.user
		user.first_name = request.POST.get('first_name')
		user.last_name =  request.POST.get('last_name')
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.save()
		return redirect('myaccount')

	context ={
		'page' : request.user.get_full_name

	}

	return render(request, 'core/edit_my_account.html', context)