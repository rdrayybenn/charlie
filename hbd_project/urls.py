from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('rides/', include('rides.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
