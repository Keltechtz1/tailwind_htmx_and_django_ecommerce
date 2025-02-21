from django.shortcuts import render, redirect
# Create your views here.

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


from .models import *
from cart.cart import Cart


def start_order(request):
	cart = Cart(request)
	if request.method == "POST":
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		region = request.POST.get('region')
		address = request.POST.get('address')

	

		order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, phone=phone, region=region, address=address)

		for item in cart:
			product = item['product']
			quantity = int(item['quantity'])
			price = product.price * quantity
			item = OrderItem.objects.create(order=order, product=product,price=price, quantity=quantity)
		# clear cart
		cart.clearCart()
		return redirect('myaccount')
	return redirect('cart')

