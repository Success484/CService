from django.db import models
import random, string

# Create your models here.

def generate_tracking_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]

    tracking_number = models.CharField(max_length=12, unique=True, default=generate_tracking_number, editable=False)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_email = models.EmailField(max_length=200)
    pickup_address = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    goods_description = models.TextField()
    weight = models.FloatField(default=0.5)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='pending')
    current_address = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tracking_number} - {self.sender_name} to {self.receiver_name}"

class TrackingEvent(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_transit", "In Transit"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
        ("failed_attempt", "Failed Attempt"),
        ("returned", "Returned"),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="events")
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="pending")
    note = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.order.tracking_number} - {self.status} at {self.location}"
