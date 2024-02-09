from django.db import models


# Create your models here.
class People(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='ПIБ')
    order_position = models.CharField(max_length=200, verbose_name='Посада')
    order_date = models.DateTimeField(auto_now=True, verbose_name='Дата прийому')
    order_email = models.CharField(max_length=200, verbose_name='Email')

    def __str__(self):
        return self.order_name