from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views #import this
from . import views

urlpatterns = [
	path('<str:product>/',views.productDetails, name='product'),
	

	]