from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    works = models.ManyToManyField('Work')


class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'
    WORK_TYPES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=WORK_TYPES)




@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)