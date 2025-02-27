from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [
    # path('', views.index_page),
    # path('app/', include('app.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
