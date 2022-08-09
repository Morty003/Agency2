from django.db import models
from uuid import uuid4
from os import path

class Service(models.Model):
    icons = (
        ("fas fa-shopping-cart fa-stack-1x fa-inverse", 'Shopping'),
        ("fas fa-laptop fa-stack-1x fa-inverse", 'Laptop'),
        ("fas fa-lock fa-stack-1x fa-inverse", 'Security'),

    )

    name = models.CharField(max_length=50, verbose_name='Название услуги')
    desc = models.CharField(max_length=200, verbose_name='Описание')
    icon = models.CharField(choices=icons, max_length=200, verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервис'



class Portfolio(models.Model):
    possition = (
        ('col-lg-4 col-sm-6 mb-4', "1"),
        ('col-lg-4 col-sm-6 mb-4', "2"),
        ('col-lg-4 col-sm-6 mb-4', "3"),
        ('col-lg-4 col-sm-6 mb-4 mb-lg-0', "4"),
        ('col-lg-4 col-sm-6 mb-4 mb-sm-0', "5"),
        ('col-lg-4 col-sm-6', "6"),
    )

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/portfolio', filename)


    name = models.CharField(max_length=50, verbose_name='Название')
    desc = models.CharField(max_length=100, verbose_name='Описание')
    photo = models.ImageField(upload_to=get_file_name, verbose_name='Фото')
    possition = models.CharField(choices=possition, max_length=50, verbose_name='Позиция', default='')
    big_desc = models.CharField(max_length=500, verbose_name='Большое описание', default='')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'



class About(models.Model):
    def get_file_name2(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/about', filename)

    name = models.CharField(max_length=50, verbose_name='Название')
    desc = models.CharField(max_length=500, verbose_name='Описание')
    photo = models.ImageField(upload_to=get_file_name2, verbose_name='Фото')
    date = models.CharField(max_length=50, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

class Team(models.Model):
    def get_file_name3(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/team', filename)


    name = models.CharField(max_length=50, verbose_name='Имя и Фамилия')
    post = models.CharField(max_length=50, verbose_name='Должность')
    photo = models.ImageField(upload_to=get_file_name3, verbose_name='Фото')
    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'



class ContactMessage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя и Фамилия')
    email = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')


    class Meta:
        verbose_name = 'Сообщениe клиента'
        verbose_name_plural = 'Сообщения клиентов'


class Clients(models.Model):
    def getfilename4(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/clients', filename)

    name = models.CharField(max_length=50, verbose_name='Имя партнёра')
    logo = models.ImageField(upload_to=getfilename4, verbose_name='Логотип партнёра')
    link = models.URLField(verbose_name='Ссылка на сайт партнёра')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Footer(models.Model):
    twitter = models.URLField()
    facebook = models.URLField()
    linkedin = models.URLField()
    privacy_policy = models.URLField(verbose_name='Пользовательское соглашение', blank=True)

    class Meta:
        verbose_name = 'Нижняя строка'
        verbose_name_plural = 'Нижняя строка'