from django.contrib import admin
from .models import ApartmentDetails, Request, Notification

admin.site.register(ApartmentDetails)
admin.site.register(Request)
admin.site.register(Notification)
