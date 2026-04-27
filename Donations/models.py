from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

from django.db import models
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
