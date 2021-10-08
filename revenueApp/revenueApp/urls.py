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
from django.conf.urls import url
from app.swagger import get_swagger_view

schema_view = get_swagger_view(title='Revenue App API')


# router = routers.DefaultRouter()
# router.register(r'revenue', views.RevenueViewSet, basename='revenue')

urlpatterns = [
    path(r'', schema_view),
    path('company', views.CompanyList.as_view()),
    path('company/<int:pk>', views.CompanyDetail.as_view()),
    path('revenue', views.RevenueList.as_view()),
    path('revenue/<int:pk>', views.RevenueDetail.as_view()),
    path('sales/hourly', views.TotalSales.as_view()),
    path('sales/daily', views.TotalSales.as_view()),
    path('admin/', admin.site.urls),
    path('ping/', views.ping),
]
