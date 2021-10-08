"""revenueApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework import routers
from app import views

# router = routers.DefaultRouter()
# router.register(r'revenue', views.RevenueViewSet, basename='revenue')

urlpatterns = [
    path('company', views.CompanyList.as_view()),
    path('company/<int:pk>', views.CompanyDetail.as_view()),
    path('revenue', views.RevenueList.as_view()),
    path('revenue/<int:pk>', views.RevenueDetail.as_view()),
    re_path(r'sales/(?P<string>hourly|daily)', views.TotalSales.as_view()),
    path('admin/', admin.site.urls),
    path('ping/', views.ping),

]
