from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views #import this
from . import views

urlpatterns = [
	path('start_order/',views.start_order, name='start_order'),
]