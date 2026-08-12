from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RentalsViewSet, VehiculoViewSet

router = DefaultRouter()
router.register(r"Rentas", RentalsViewSet, basename="rentas")
router.register(r"vehiculos", VehiculoViewSet, basename="vehiculos")

urlpatterns = []
urlpatterns += router.urls