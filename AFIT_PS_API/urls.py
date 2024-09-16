from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('payment.urls')),
]
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "AeroPay Admin"  # Customize the site header
admin.site.site_title = "AeroPay Title"  # Customize the title that appears on the browser tab
admin.site.index_title = "Welcome to AeroPay Admin Portal"  # Customize the index title