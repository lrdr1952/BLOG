#from cloudinary.models import CloudinaryField
from decouple import config
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #photo = CloudinaryField('image')
    photo = models.ImageField(upload_to='Profiles',blank=False, null=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Bienvenido a ABC BLOG',
            str('Hola ' + instance.full_name + ', usted se ha registrado satisfactoriamente.'),
            'abc.micompany@gmail.com',
            [instance.email]
        )