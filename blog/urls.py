from django.urls import path

from .views import home, more

urlpatterns = [
    path('', home, name="home"),
    path('more/<int:id>', more, name="more"),
]