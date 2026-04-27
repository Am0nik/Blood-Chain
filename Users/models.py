from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    BLOOD_TYPES = [
        ('1+', 'I (O) Rh+'),
        ('1-', 'I (O) Rh-'),
        ('2+', 'II (A) Rh+'),
        ('2-', 'II (A) Rh-'),
        ('3+', 'III (B) Rh+'),
        ('3-', 'III (B) Rh-'),
        ('4+', 'IV (AB) Rh+'),
        ('4-', 'IV (AB) Rh-'),
    ]
     
    name = models.CharField(max_length=150, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    photo = ResizedImageField(
        size=[300, 300],      # Максимальный размер (впишет в эти рамки)
        crop=['middle', 'center'], # Обрежет по центру, чтобы было красиво
        quality=75,           # Качество в % (75 — золотая середина)
        upload_to='user_photos/', 
        force_format='JPEG',  # Всегда сохранять как легкий JPEG
        blank=True, 
        null=True
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    blood_type = models.CharField(
        max_length=3, 
        choices=BLOOD_TYPES, 
        blank=True, 
        null=True
    )
    terms = models.BooleanField(default=False, verbose_name="Accept Terms and Conditions")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email