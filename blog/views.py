from django.shortcuts import render
from .models import Category, News

# Create your views here.
def home(request):
    
    last = News.objects.filter(isFeatured=True).order_by('-created').first()

    newss = News.objects.order_by('-created')

    return render(request, "home.html", { 'last': last, 'newss': newss})


def more(request, id):
    news = News.objects.get(id=id)
    return render(request, "more.html", {"news":news})