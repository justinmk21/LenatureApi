from django.db import models
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('best_seller', 'Best Seller'),
    ]

    TYPE_CHOICES = [
        ('face', 'Face'),
        ('body', 'Body'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='face')
    image = CloudinaryField('image', default=None)

    def __str__(self):
        return self.name
