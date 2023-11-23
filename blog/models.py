from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Төрлийн нэр')
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Мэдээний төрөл")
        verbose_name_plural = ("1.1 Мэдээний төрлүүд")

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Гарчиг', null=True)
    shortBody = models.CharField(max_length=255, verbose_name='Товч агуулга ')
    body = RichTextUploadingField(verbose_name='Агуулга')
    image = models.ImageField(upload_to="news/%Y/%m/%d/", verbose_name='Зураг')
    isFeatured = models.BooleanField(default=0, verbose_name='Онцлох')

    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Огноо')
    categories = models.ManyToManyField(Category, verbose_name='Мэдээний төрөл')
    

    class Meta:
        verbose_name = ("Вэб мэдээ")
        verbose_name_plural = ("1.2 Вэб мэдээнүүд")

    def __str__(self):
        return self.title