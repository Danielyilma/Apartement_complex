# myapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Request
from UserAccountManager.models import User

@receiver(post_save, sender=Request)
def send_notification(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    group_name = f'user_{instance.user.id}'
    print("dddddddddddddddddddddddddddd", group_name)
    if created:
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_notification',
                'message': f'request {instance.title} submited successfully'
            }
        )
    else:
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_notification',
                'message': f'request {instance.title} submited successfully'
            }
        )
