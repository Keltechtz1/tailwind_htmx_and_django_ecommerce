from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views #import this
from . import views

urlpatterns = [
		path('add-to-cart/<int:product_id>/',views.add_to_cart, name='add_to_cart'),
		path('add-to-cart/<int:product_id>/<str:action>/update/',views.update_cart, name='update_cart'),
		path('shopping-cart/',views.cartView, name='cart'),
		path('checkout/',views.checkoutView, name='checkout'),
		path('hx_menu_cart/',views.hx_menu_cart, name='hx_menu_cart'),
		path('hc_cart_total/',views.hx_cart_total, name='hx_cart_total'),

	]