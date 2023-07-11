from django.db import models
from django.contrib.auth.models import User

from .utils import (rename_path, adding_watermark, DEFAULT_CLIENT_IMAGE_PATH)


class Client(models.Model):
    """
    Модель описывающая клиентов приложения
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    GENDERS = (
        ('М', 'Мужской'),
        ('Ж', 'Женский')
    )

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    gender = models.CharField(verbose_name='Пол', max_length=1, choices=GENDERS, default='М')
    image = models.ImageField(verbose_name='Аватар', upload_to=rename_path, blank=True,
                              default=r"static/clients/images/default.png")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image.path != DEFAULT_CLIENT_IMAGE_PATH:
            adding_watermark(self.image.path)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Likes(models.Model):
    """
    Модель, которая описывает симпатии клиентов
    """
    class Meta:
        ordering = ['id']
        verbose_name = 'Симпатия'
        verbose_name_plural = 'Симпатии'

    from_client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='От клиента',
                                    related_name='from_client')
    to_client = models.ForeignKey(to=Client, on_delete=models.CASCADE, verbose_name='К клиента',
                                  related_name='to_client')

    def __str__(self):
        return f'Симпатия {self.from_client} к {self.to_client}'

