# Generated by Django 4.2.3 on 2023-07-11 18:30

import clients.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_options_remove_client_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.ImageField(blank=True, default='static/clients/images/default.png', upload_to=clients.utils.rename_path, verbose_name='Аватар'),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_client', to='clients.client', verbose_name='От клиента')),
                ('to_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_client', to='clients.client', verbose_name='К клиента')),
            ],
            options={
                'verbose_name': 'Симпатия',
                'verbose_name_plural': 'Симпатии',
                'ordering': ['id'],
            },
        ),
    ]
