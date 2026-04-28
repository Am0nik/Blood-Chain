from django.contrib import admin
from .models import News, BloodInventory, Donation
# Register your models here.
admin.site.register(News)
admin.site.register(BloodInventory)
admin.site.register(Donation)