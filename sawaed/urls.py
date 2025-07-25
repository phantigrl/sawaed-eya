"""
URL configuration for sawaed project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pages import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('content/', views.content, name='content'),
    path('intro/', views.intro, name='intro'),
    path('team/', views.team, name='team'),
    path('services/', views.services, name='services'),
    path('case/', views.case, name='case'),
    path('vision/', views.vision, name='vision'),
    path('aims/', views.aims, name='aims'),
    path('contact/', views.contact, name='contact'),
    path('job_seekers/', views.job_seekers, name='job_seekers'),

]

import os

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'pages/static'))
