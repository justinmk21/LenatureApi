from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('best_seller', 'Best Seller'),
        ('none', 'None'),
    ]

    TYPE_CHOICES = [
        ('face', 'Face'),
        ('body', 'Body'),
        ('hair', 'Hair'),
    ]

    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True)
    quantity = models.PositiveIntegerField()
    discounted_price = models.IntegerField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='face')
    image = models.URLField()

    def __str__(self):
        return self.name
