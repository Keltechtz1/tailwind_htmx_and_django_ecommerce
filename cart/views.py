from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .cart import Cart
from products.models import Product

def add_to_cart(request, product_id):
	cart = Cart(request)
	cart.add(product_id)

	return render(request, 'cart/menu_cart.html')


def cartView(request):

	context = {
		'page': 'Cart Page'
	}

	return render(request, 'cart/cart.html', context)

def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'item_image': product.item_image,
                'get_thumbnail': product.get_thumbnail,
                'price': product.price
            },
            'total_price': (product.price * quantity),
            'quantity': quantity
        }
    else:
        item = None

    response = render(request, 'cart/partials/cart_items.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response



@login_required
def checkoutView(request):
    cart = Cart(request)
    print(str(cart.get_total_cost))
    context = {
		'page': 'Checkout'
	}

    return render(request, 'cart/checkout.html', context)



def hx_menu_cart(request):
	return render(request, 'cart/menu_cart.html')



def hx_cart_total(request):
	return render(request, 'cart/partials/cart_total.html')