from django.db import models
from base_model import TimeStampMixin


class ApartmentDetails(TimeStampMixin, models.Model):
    about = models.TextField()
    name = models.CharField(max_length=60, blank=True)
    block = models.CharField(max_length=60, blank=True)
    contact_email = models.CharField(max_length=60, blank=True)
    contact_phone = models.CharField(max_length=60, blank=True)

class Request(TimeStampMixin, models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    user = models.ForeignKey('UserAccountManager.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')

    def __str__(self):
        return f"Request by {self.user.first_name} - {self.title} ({self.status})"

class Notification(TimeStampMixin, models.Model):
    user = models.ForeignKey('UserAccountManager.User', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {'Read' if self.is_read else 'Unread'}"

class WaterSensor(models.Model):
    percentage = models.CharField(max_length=150)