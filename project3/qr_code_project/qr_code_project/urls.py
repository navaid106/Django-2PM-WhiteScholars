
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('qr/', views.generate_qr_code, name='generate_qr_code')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
