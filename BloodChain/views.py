from django.shortcuts import render
from Donations.models import News, BloodInventory
# Create your views here.
def index(request):
    news = News.objects.all()[:4]
    blood_inventory = BloodInventory.objects.all()
    return render(request, 'index.html', {'news': news, 'blood_stocks': blood_inventory})