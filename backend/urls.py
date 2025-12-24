from django.contrib import admin
from django.urls import path
from routing.views import health, route_with_fuel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('api/route/', route_with_fuel),
]
