from django.db import models


class Product(models.Model):
    """This model is for create product"""
    category_choices = [
        ("laptops", "laptops"),
        ('smartphones', 'smartphones'),
        ('accessories', "accessories")
    ]
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=category_choices)

    def __str__(self):
        return f"{self.name}"
