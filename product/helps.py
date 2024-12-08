import uuid


class SaveImages(object):
    def product_images_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f"product/{uuid.uuid4()}.{image_extension}"