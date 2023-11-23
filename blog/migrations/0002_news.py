# Generated by Django 4.2.7 on 2023-11-23 04:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Гарчиг')),
                ('shortBody', models.CharField(max_length=255, verbose_name='Товч агуулга ')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Агуулга')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='Зураг')),
                ('isFeatured', models.BooleanField(default=0, verbose_name='Онцлох')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Огноо')),
                ('categories', models.ManyToManyField(to='blog.category', verbose_name='Мэдээний төрөл')),
            ],
            options={
                'verbose_name': 'Вэб мэдээ',
                'verbose_name_plural': '1.2 Вэб мэдээнүүд',
            },
        ),
    ]
