from django import template
register = template.Library()

from blog.models import Category



@register.inclusion_tag('tags/categories.html')
def get_category():
   
    categories = Category.objects.all()

    return { 'categories': categories }