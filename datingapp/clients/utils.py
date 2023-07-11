from PIL import Image


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
    watermark = Image.open(r'static/clients/images/watermark.png')
    image.paste(watermark, (0, 0))
    image.save(image_path)


# Path to default.png.

DEFAULT_CLIENT_IMAGE_PATH = 'static/clients/images/default.png'

