from django.urls import path
from main_app.views import indexPage
from main_app.views import indexPage, tracking_detail

urlpatterns = [
    path('', indexPage, name="home"),
    path("track/<str:tracking_number>/", tracking_detail, name="tracking_detail"),
]