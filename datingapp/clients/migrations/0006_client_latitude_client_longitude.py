# Generated by Django 4.2.3 on 2023-07-12 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_alter_likes_from_client_alter_likes_to_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=7, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=8, verbose_name='Долгота'),
        ),
    ]
