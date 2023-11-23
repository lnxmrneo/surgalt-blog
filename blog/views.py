from django.shortcuts import render
from .models import Category, News

# Create your views here.
def home(request):
    categories = Category.objects.all()
    last = News.objects.filter(isFeatured=True).order_by('-created').first()

    newss = News.objects.order_by('-created')

    return render(request, "home.html", {'categories':categories, 'last': last, 'newss': newss})