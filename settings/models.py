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

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "настройки"
        verbose_name_plural = "настройка"

class About(models.Model):
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    def __str__(self):
        return self.descriptions
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Program(models.Model):
    school_program =models.TextField(
        verbose_name="школьная программа"
    )

    def __str__(self):
        return self.school_program 
    class Meta:
        verbose_name = "программа"

        
class Teacher(models.Model):
    our_teachers = models.TextField(
        verbose_name="Наши учетеля"
    )
    def __str__(self):
        return self.our_teachers
    class Meta:
        verbose_name = "учителя"
    