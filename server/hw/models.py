from django.db import models


class First(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(verbose_name='Полное имя', max_length=150)

    def __str__(self):
        return f'[{self.id}] {self.full_name}'


class Second(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.CharField(verbose_name='Местоположние', max_length=150)
    car = models.CharField(verbose_name='Информация о машине', max_length=150)
    number = models.CharField(verbose_name='Рег номер', max_length=150)
    fk = models.ForeignKey('First', on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.id}] {self.name}'

