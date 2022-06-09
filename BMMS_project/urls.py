"""BMMS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from home_page.views import user_logout, blood_order, after_login_home, order_details_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('logout',user_logout,name='logout'),
    path('blood_order', blood_order,name='blood_order'),
    path('after_login',after_login_home, name='after_login'),
    path('order_details_page',order_details_page, name='order_details_page'),
]
