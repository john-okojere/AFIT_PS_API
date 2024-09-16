from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('payment.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from django.utils.translation import gettext_lazy as _

admin.site.site_header = "AeroPay Admin"  # Customize the site header
admin.site.site_title = "AeroPay Title"  # Customize the title that appears on the browser tab
admin.site.index_title = "Welcome to AeroPay Admin Portal"  # Customize the index title
