"""iCrawler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
     path('', views.get_status),
    # url(r'^api/crawl/', views.crawl, name='crawl'),
]