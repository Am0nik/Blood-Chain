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
        size=[300, 300], 
        crop=['middle', 'center'],
        quality=75,
        upload_to='user_photos/', 
        force_format='JPEG',
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

    number_of_donations = models.PositiveIntegerField(default=0)
    rank = models.CharField(max_length=20, default='Novice')

    def save(self, *args, **kwargs):
        if self.number_of_donations >= 10:
            self.rank = 'Legendary Hero'
        elif self.number_of_donations >= 5:
            self.rank = 'Hero'
        elif self.number_of_donations >= 1:
            self.rank = 'Kind Soul'
        else:
            self.rank = 'Novice'
        super().save(*args, **kwargs)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email