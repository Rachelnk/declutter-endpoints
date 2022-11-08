from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_seller:
            Seller.objects.create(user=instance)
        elif instance.is_buyer:
            Buyer.objects.create(user=instance)
            


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if instance.is_seller:
        instance.seller.save()
    elif instance.is_buyer:
        instance.buyer.save()

