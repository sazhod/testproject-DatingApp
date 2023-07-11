# Generated by Django 4.2.3 on 2023-07-11 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0003_alter_client_image_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='from_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_client', to=settings.AUTH_USER_MODEL, verbose_name='От клиента'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='to_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_client', to=settings.AUTH_USER_MODEL, verbose_name='К клиента'),
        ),
    ]
