from urllib import response

from django.db import models
from ckeditor.fields import RichTextField
import requests
from urllib.parse import quote
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

from django.core.validators import MinValueValidator, MaxValueValidator

class BloodInventory(models.Model):
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

    blood_type = models.CharField(
        max_length=3, 
        choices=BLOOD_TYPES, 
        unique=True,
        verbose_name="Blood Type"
    )
    percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=50,
        help_text="Inventory level in percentage (0-100)",
    )
    @property
    def status(self):
        if self.percentage < 25:
            return "CRITICAL"
        elif self.percentage < 60:
            return "STABLE"
        else:
            return "FULL"

    class Meta:
        verbose_name = "Blood Inventory"
        verbose_name_plural = "Blood Inventories"
        ordering = ['blood_type']

    def __str__(self):
        return f"{self.get_blood_type_display()}: {self.percentage}%"


from django.dispatch import receiver
from django.db import transaction

class Donation(models.Model):
    user = models.ForeignKey('Users.User', on_delete=models.CASCADE, related_name='my_donations')
    amount = models.PositiveIntegerField(default=450, help_text="Amount of blood donated in ml")
    date = models.DateTimeField(auto_now_add=True)
    blood_type_at_donation = models.CharField(max_length=3, editable=False)

    class Meta:
        verbose_name = "Blood Donation"
        verbose_name_plural = "Blood Donations"

    def save(self, *args, **kwargs):
        if not self.pk:
            with transaction.atomic():
                self.blood_type_at_donation = self.user.blood_type
                self.user.number_of_donations += 1
                from .models import BloodInventory
                inventory, _ = BloodInventory.objects.get_or_create(
                    blood_type=self.blood_type_at_donation
                )
                
                added_val = (self.amount / 450) * 1 # 450мл =1%
                inventory.percentage = min(inventory.percentage + added_val, 100)
                


                inventory.save()
                self.user.save()
                
                super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Donation {self.user.username} - {self.date.strftime('%d.%m.%Y')}"




class DonationNeed(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.address and (self.lat is None or self.lon is None):
            try:
                clean_address = self.address.strip()

                url = "https://nominatim.openstreetmap.org/search"
                params = {
                    "q": clean_address,
                    "format": "json",
                    "limit": 1,
                    "addressdetails": 1
                }

                headers = {
                    "User-Agent": "BloodChainApp/1.0"
                }

                response = requests.get(
                    url,
                    params=params,
                    headers=headers,
                    timeout=10
                )

                data = response.json()

                print("Searching:", clean_address)
                print("Result:", data)

                if data:
                    self.lat = float(data[0]["lat"])
                    self.lon = float(data[0]["lon"])

            except Exception as e:
                print("Error geocoding:", e)

        super().save(*args, **kwargs)