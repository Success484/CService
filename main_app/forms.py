from django import forms
from main_app.models import Order, TrackingEvent

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["sender_name", "receiver_name", "pickup_address", "delivery_address", "goods_description", "weight", "payment_status"]

class TrackingEventForm(forms.ModelForm):
    class Meta:
        model = TrackingEvent
        fields = ["location", "status", "note", "latitude", "longitude"]