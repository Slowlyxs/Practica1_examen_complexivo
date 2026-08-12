from rest_framework import serializers
from .models import Rentals, Vehiculo

class RentalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentals
        fields = ["id", "vehicle_id", "customer_name", "total", "status", "created_at"]

class VehiculoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.CharField(source="marca.nombre", read_only=True)

    class Meta:
        model = Vehiculo
        fields = ["id", "plate", "brand", "daily_rate", "is_available", "marca_nombre"]