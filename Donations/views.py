from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
import html
from .models import DonationNeed
# Create your views here.

def news(request, id):
    news_item = get_object_or_404(News, pk=id)
    news_item.content = html.unescape(news_item.content)
    return render(request, 'news.html', {'news_item': news_item})

def map(request):
    centers = DonationNeed.objects.all()

    print("TOTAL:", centers.count())
    print("WITH LAT:", centers.filter(lat__isnull=False).count())

    return render(request, 'map.html', {'centers': centers})