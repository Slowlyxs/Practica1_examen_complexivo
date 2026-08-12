from django.db import models

class Vehiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=40)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.brand} {self.plate}"

class Rentals(models.Model):
    id = models.BigAutoField(primary_key=True)
    vehicle_id = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=120)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Rental {self.id} for {self.customer_name} - Vehicle: {self.vehicle_id.plate}"