from django.conf import settings

from products.models import Product


class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)

		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}

		self.cart = cart


	# get all items in the cart
	def __iter__(self):
		for p in self.cart.keys():
			self.cart[str(p)]['product'] = Product.objects.get(pk=p)


		for item in self.cart.values():
			item['total_price'] = item['product'].price * item['quantity']

			yield item

	# get number of items in the cart
	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	# save cart

	def save(self):
		self.session[settings.CART_SESSION_ID] = self.cart
		self.session.modified = True

	# add thing to the cart
	def add(self, product_id, quantity=1, update_quantity=False):
		product_id = str(product_id)

		if product_id not in self.cart:
			self.cart[product_id] = {'quantity' : 1, 'id': product_id}

		if update_quantity:
			self.cart[product_id]['quantity'] += int(quantity)

			# check if quantity is zero remove from the cart
			if self.cart[product_id]['quantity'] == 0:
				self.remove(product_id)


		self.save()


	def remove(self, product_id):
		if product_id in self.cart:
			del self.cart[product_id]  

			self.save()

	def clearCart(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True


	def get_total_cost(self):
		for p in self.cart.keys():
			self.cart[str(p)]['product'] = Product.objects.get(pk=p)

		return sum(item['product'].price * item['quantity'] for item in self.cart.values()) 


	def get_item(self, product_id):
		if str(product_id) in self.cart:
			return self.cart[str(product_id)]
		else:
			return None






