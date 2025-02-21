from django.shortcuts import render,  redirect,get_object_or_404

# Create your views here.

# Create your views here.

from .models import *

def productDetails(request, product):
	item = get_object_or_404(Product, slug=product)
	context = {
			'page_home' : 'home',
			'item' : item
	}
	return  render(request, 'products/product_details.html', context)

