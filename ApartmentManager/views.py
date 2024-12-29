from rest_framework import generics, serializers
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializer import ApartementSerializer, RequestSerializer
from UserAccountManager.models import User
from .models import Request, ApartmentDetails, Notification, WaterSensor


class UserApartmentView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ApartementSerializer

    def get_object(self):
        user = self.request.user

        if hasattr(user, 'apartment') and user.apartment:
            return user.apartment
        else:
            raise serializers.ValidationError("This user is not associated with any apartment.")
        
class RequestView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user
        return Request.objects.filter(user_id=user.id)


class RequestCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

class UserApartmentCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ApartementSerializer

class ApartmentsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ApartementSerializer
    queryset = ApartmentDetails.objects.all()

class StatusView(APIView):

    def get(self, request, format=None):
        user_c = User.objects.all().count()
        apartment_C = ApartmentDetails.objects.all().count()
        request_c = Request.objects.all().count()
        Notification_c = Notification.objects.all().count()

        data = {
            'users': user_c,
            'apartments': apartment_C,
            'requests': request_c,
            'notifications': Notification_c
        }

        return Response(data)

class SensorData(APIView):

    def get(self, request, format=None):
        data = request.query_params.get('data')
        w_sensor = WaterSensor.objects.first()
        w_sensor.percentage = data

        return Response()
