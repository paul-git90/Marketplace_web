from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal=2)
    image = models.ImageField(upload_to='product_images/', null=True)
    ingredients = models.TextField()
    weight_grams = models.PositiveIntegerField(default=0)
    available_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    