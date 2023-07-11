# Generated by Django 4.2.3 on 2023-07-11 14:44

import clients.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id'], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], default='М', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(blank=True, upload_to=clients.models.rename_path, verbose_name='Аватар'),
        ),
    ]