from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import MyProfile
from django.conf import settings

@receiver(post_save, sender=User)
def save_Profile(sender,instance, created ,**wk):
    if created:
        MyProfile.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created,**kwargs):
        if not created:
             return
             # Create the profile object, only if it is newly created
             profile = models.Profile(user=instance)
             profile.save()