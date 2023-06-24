from django.urls import path
from . consumers import DashboardConsumer

# route api

websocket_urlpatterns = [
    path('ws/<str:dashbaord_slug>/', DashboardConsumer.as_asgi()),
]