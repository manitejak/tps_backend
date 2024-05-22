"""
URL configuration for tps_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import routers
from tenders.views import (
    TenderViewSet, AccountViewSet, StateViewSet, CityViewSet, BrandViewSet,
    ContractDurationViewSet, MonthViewSet, DistributorViewSet,TenderBViewSet
)

router = routers.DefaultRouter()
router.register(r'tenders', TenderViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'contract_durations', ContractDurationViewSet)
router.register(r'months', MonthViewSet)
router.register(r'distributors', DistributorViewSet)
router.register(r'btenders', TenderBViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
