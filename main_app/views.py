from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render 
from django.contrib import messages
from main_app.models import Order
import json


# Create your views here.
def indexPage(request):
    tracking_number = request.GET.get("tracking_number")

    if tracking_number:
        try:
            order = Order.objects.get(tracking_number=tracking_number)
            return redirect("tracking_detail", tracking_number=order.tracking_number)
        except Order.DoesNotExist:
            messages.error(request, "❌ Invalid Tracking Code. Please try again.")
            return redirect("home")  # make sure 'index' is the name of your home URL

    return render(request, "pages/index.html")


def tracking_detail(request, tracking_number):
    order = get_object_or_404(Order, tracking_number=tracking_number)

    # collect events with coordinates (asc order for route path)
    events_qs = order.events.order_by('timestamp')  # ascending
    events_list = []
    for e in events_qs:
        if e.latitude is not None and e.longitude is not None:
            events_list.append({
                "status": e.status,
                "location": e.location,
                "note": e.note,
                "timestamp": e.timestamp.isoformat(),
                "lat": float(e.latitude),
                "lng": float(e.longitude),
            })

    events_json = json.dumps(events_list)  # will be escaped in template
    return render(request, "pages/tracking_detail.html", {
        "order": order,
        "events_json": events_json,
    })