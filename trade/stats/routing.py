from django.urls import path
from . consumers import DashboardConsumer

# django channels api route

websocket_urlpatterns = [
    path('ws/<str:dashbaord_slug>/', DashboardConsumer.as_asgi()),
]