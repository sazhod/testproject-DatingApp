from PIL import Image
from django.conf import settings
from django.core.mail import EmailMessage, get_connection


def rename_path(instance: 'Client', filename: str) -> str:
    """
    Метод, который отвечает за изменение названия изображения.
    instance: Client - Объект нашего клиента
    filename: str - Оригинальный путь к изображению
    :return -> str
    """
    upload_to = 'static/clients/images/'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = f'{instance.pk}.{ext}'

    return f'{upload_to}{filename}'


def adding_watermark(image_path: str) -> None:
    """
    Метод, который отвечает за добавление вотермарки на изображение пользователя.
    :param image_path: str Путь до изображения пользователя.
    """
    image = Image.open(image_path)
    watermark = Image.open(WATERMARK_IMAGE_PATH)
    image.paste(watermark, (0, 0))
    image.save(image_path)


def send_email(from_client, to_client):
    with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
    ) as connection:
        subject = 'Взаимная симпатия'
        email_from = from_client.user.email
        recipient_list = [to_client.user.email, ]
        message = f'Вы понравились "{from_client}"!\nПочта участника: "{from_client.user.email}"'
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()


# Path to default.png.

DEFAULT_CLIENT_IMAGE_PATH = r'static/clients/images/default.png'
WATERMARK_IMAGE_PATH = r'static/clients/images/watermark.png'
