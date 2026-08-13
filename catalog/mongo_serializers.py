from rest_framework import serializers


class RentalEventsSerializer(serializers.Serializer):
    rental_id = serializers.CharField(max_length=120)
    event_type = serializers.CharField(max_length=20)  # (CREATED, PICKED_UP, RETURNED, PAID, CANCELLED)
    source = serializers.CharField(max_length=20, required=False)  # (WEB, MOBILE, SYSTEM)
    note = serializers.CharField(required=False, allow_blank=True)
    created_at = serializers.DateField(required=False)

class FleetLogsSerializer(serializers.Serializer):
    vehiculo_id = serializers.IntegerField()        # ID de Vehiculo (Postgres)
    action = serializers.CharField(max_length=20)
    note = serializers.CharField(required=False, allow_blank=True)
    source = serializers.CharField(max_length=20, required=False)  # (SYSTEM, MOBILE)
    # (CREATED, UPDATED, MAINTENANCE, DISABLED)
    created_at = serializers.DateField(required=False)
