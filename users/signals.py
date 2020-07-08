# signal that gets fired after an user is saved
from django.db.models.signals import post_save
# user is the sender, because sends the signal
from django.contrib.auth.models import User
# receiver get the signal and perform some tasks
from django.dispatch import receiver
from .models import Profile

# when a user is saved, then send signal(post_save).
# Signal will be received by @receiver.
# The receiver is create_profile function.
# The function takes all the arguments that post_save signal passed.
# If the user was created, then create a profile object with the user=instance of the user that was created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

