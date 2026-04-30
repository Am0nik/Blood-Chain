from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
# Create your views here.
def map(request):
    return render(request, 'map.html')

def news(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news.html', {'news_item': news_item})