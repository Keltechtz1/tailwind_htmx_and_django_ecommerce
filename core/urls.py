from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views #import this
from . import views

urlpatterns = [
	path('',views.homeView, name='home'),
	path('signup/',views.signUpView, name='sign_up'),
	path('login/',views.loginView, name='login'),
	path('products/',views.shopView, name='shop'),

	# my account
	path('myaccount/', views.myAccount, name='myaccount'),
	path('edit-myaccount/', views.editMyAccount, name='edit_myaccount'),

	path('logout/',auth_views.LogoutView.as_view(), name='logout'),

	]