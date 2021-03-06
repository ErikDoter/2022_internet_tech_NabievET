# Generated by Django 4.0.1 on 2022-01-16 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150, verbose_name='Полное имя')),
            ],
        ),
        migrations.CreateModel(
            name='Second',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('place', models.CharField(max_length=150, verbose_name='Местоположние')),
                ('car', models.CharField(max_length=150, verbose_name='Информация о машине')),
                ('number', models.CharField(max_length=150, verbose_name='Рег номер')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw.first')),
            ],
        ),
    ]
