from django.db import models

from django.contrib.auth.models import User

from products.models import Product
# Create your models here.
class Order(models.Model):
	STATUS_CHOICES=(
		('Pending', 'Pending'), 
		('Shipped', 'Shipped'), 
		('Completed', 'Completed'), 
		('Canceled','Canceled'),
	)

	user = models.ForeignKey(User, related_name='orders', blank=True, null=True, on_delete=models.CASCADE,)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	address = models.CharField(max_length=255)
	region = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	is_paid = models.BooleanField(default=False)
	paid_amount =  models.PositiveIntegerField(blank=True, null=True)
	status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Pending')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Orders'

	def get_total_price(self):
		return None

	def __str__(self):
		return f"Order {self.id} in {self.user.username} TZS {self.paid_amount}"


class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
	price =  models.PositiveIntegerField()
	quantity =  models.PositiveIntegerField()

	def get_total_price(self):
		return self.price
