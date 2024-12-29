from rest_framework import serializers
from .models import ApartmentDetails, Request

class ApartementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ApartmentDetails
        fields = ['about', 'name', 'block', 'contact_email', 'contact_phone']

class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = ['title', 'description', 'status', 'created_at']
    
    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user'] = request.user
        return super().create(validated_data)