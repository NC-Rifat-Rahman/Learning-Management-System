from datetime import timedelta,datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.urls import reverse
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse as api_reverse
import jwt

class UserProfile(models.Model):
    #email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    #id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile',
        null=True, blank=True
    )
    description = models.TextField()
    def __str__(self):
        return self.user.username

    @property
    def owner(self):
        return self.user
    @property
    def token(self):
        token= jwt.encode({'username': self.username, 'email':self.email,
                           'exp':datetime.utcnow()+ timedelta(hours=24)},
                           settings.SECRET_KEY,algorithm='HS256')
        return token

    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud",kwargs={'pk': self.pk}, request=request)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()

"""""
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = [ 'username', 'phone', 'first_name', 'last_name'
    ]
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email



@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
"""""