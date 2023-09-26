from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    assress = models.CharField(
        max_length=500,
        verbose_name="Адрес"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="телефонный номер"
    )
    facebook_url = models.URLField(
        verbose_name="Ссылка на facebook"
    )
    instagram_url = models.URLField(
        verbose_name="Ссылка на unstagram"
    )
    linkeldin_url = models.URLField(
        verbose_name="Ссылка на Linkeldin"
    )