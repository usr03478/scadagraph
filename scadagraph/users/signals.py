from django.db.models.signals import post_save
from django.contrib.auth.models import User  # User is the sender
from django.dispatch import receiver
from .models import Profile


# post save signal when a user get created, create new profile for each created user


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_profile(sender, instance, **kwargs):
    instance.profile.save