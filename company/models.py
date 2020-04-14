from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Main(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Главная'

class About(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'О компании'

class Contacts(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Контакты'