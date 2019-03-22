"""certificate_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from generator.views import CertificateTemplateView, GenerateCertificate
import settings_local

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^certificate/templates/$', CertificateTemplateView.as_view()),
    url(r'^certificate/lists/$', GenerateCertificate.as_view())
] + static(settings_local.MEDIA_URL, document_root=settings_local.MEDIA_ROOT)
