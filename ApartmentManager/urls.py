from django.urls import path
from .views import UserApartmentView, RequestView, RequestCreateView, UserApartmentCreate, ApartmentsView, SensorData, PumpView, WaterLevel
from .consumer import NoticicationConsumer

urlpatterns = [
    path('<int:id>', UserApartmentView.as_view(), name='user_apartement'),
    path('create', UserApartmentCreate.as_view(), name='create-user-apartment'),
    path('requests/', RequestView.as_view(), name='user-request'),
    path('requests/create', RequestCreateView.as_view(), name='request-creation'),
    path('', ApartmentsView.as_view(), name='get-apartments'),
    path('sensor', SensorData.as_view(), name='water_sensor'),
    path('pump', PumpView.as_view(), name='pump-status'),
    path('level', WaterLevel.as_view(), name='water_level')
]

websocket_urlpatterns = [
    path('ws/apartment/notification/', NoticicationConsumer.as_asgi(), name="apartment-notification")
]
