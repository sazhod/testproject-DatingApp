from django.db import models
from django.contrib.auth.models import User
from os.path import join


def rename_path(instance, filename: str) -> str:
    """
    Метод, который отвечает за зменение названия изображения.
    instance: Client - Объект нашего клиента
    filename: str - Оригинальный путь к изображению
    :return -> str
    """
    print(type(instance), instance)
    upload_to = 'static/clients/'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = f'{instance.pk}.{ext}'

    return f'{upload_to}{filename}'


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
    image = models.ImageField(verbose_name='Аватар', upload_to=rename_path, blank=True)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'
