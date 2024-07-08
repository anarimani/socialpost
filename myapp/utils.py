import os
from django.conf import settings

def save_image(image):
    image_path = os.path.join(settings.MEDIA_ROOT, image.name)
    with open(image_path, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)
    return image_path
