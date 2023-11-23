from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Төрлийн нэр')
   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Мэдээний төрөл")
        verbose_name_plural = ("1.1 Мэдээний төрлүүд")