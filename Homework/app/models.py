from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Computer(models.Model):
    id_computer = models.AutoField(primary_key=True)
    name_computer = models.CharField(max_length=100, verbose_name='Компьютер')
    model_computer = models.CharField(max_length=100, verbose_name='Модель')
    company_computer = models.CharField(max_length=100, verbose_name='Производитель')
    price_computer = models.IntegerField(verbose_name='Цена')
    characteristics_computer = models.TextField(verbose_name='Характеристики')
    photo_computer = models.ImageField(null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name_computer

    class Meta:
        verbose_name_plural = "Компьютеры"
        verbose_name = "Компьютер"


class Order(models.Model):
    id_order = models.AutoField(primary_key=True, verbose_name='ID Заказа')
    id_comp = models.ForeignKey(Computer, on_delete=models.CASCADE, verbose_name='Название компьютера')
    id_user = models.ManyToManyField(User, verbose_name='ID Пользователя')

    def get_users(self):
        return [u.username for u in self.id_user.all()]
    get_users.short_description = 'Заказы пользователей'

    class Meta:
        verbose_name_plural = "Заказы"
        verbose_name = "Заказ"