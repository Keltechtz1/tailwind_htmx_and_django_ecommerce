from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# rename admin dashboard
admin.site.site_header = "Ecommerce  Portal" 
admin.site.site_title = "Ecommerce Management Portal"
admin.site.index_title = "Welcome to Ecommerce Management Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('order/', include('order.urls')),
    path('cart/', include('cart.urls')),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

