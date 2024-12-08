from django.db import models
from .helps import SaveImages


class TypeProduct(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=SaveImages.product_images_path)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def discount_price(self):
        return self.price - self.price * self.discount / 100