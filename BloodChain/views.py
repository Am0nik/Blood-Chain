from django.shortcuts import render
from Donations.models import News
# Create your views here.
def index(request):
    news = News.objects.all()[:4]
    return render(request, 'index.html', {'news': news})