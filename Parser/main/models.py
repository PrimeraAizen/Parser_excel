from django.db import models


# Create your models here.
class Employees(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    id_number = models.CharField(max_length=12, verbose_name='ИИН')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'