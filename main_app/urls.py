from django.urls import path
from main_app.views import indexPage
from main_app.views import indexPage, create_order, tracking_detail

urlpatterns = [
    path('', indexPage, name="home"),
    path('package-detail/form/', create_order, name='detail_form'),
    path("track/<str:tracking_number>/", tracking_detail, name="tracking_detail"),
]