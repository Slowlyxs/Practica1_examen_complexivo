from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import  Rentals, Vehiculo
from .serializers import RentalsSerializer, VehiculoSerializer
from .permissions import IsAdminOrReadOnly

class RentalsViewSet(viewsets.ModelViewSet):
    queryset = Rentals.objects.all().order_by("id")
    serializer_class = RentalsSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["customer_name"]
    ordering_fields = ["id", "customer_name"]

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.select_related("marca").all().order_by("-id")
    serializer_class = VehiculoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["vehicle_id"]
    search_fields = ["plate", "brand", "daily_rate", "marca_nombre"]
    ordering_fields = ["id", "daily_rate", "marca_nombre", "plate", "brand"]

    def get_permissions(self):
        # Público: SOLO listar vehículos
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()