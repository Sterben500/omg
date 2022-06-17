
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_main.urls')),
    path('crud_main', include('crud_main.urls')),
    path('', TemplateView.as_view(template_name='get_data.html'), name='dataView'),
]
