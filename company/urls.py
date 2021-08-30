from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'company'

router = routers.SimpleRouter()
router.register('companies', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
