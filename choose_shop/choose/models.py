from django.db import models

class Intorduce(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)
    date_register = models.DateField(auto_now=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    status_choieces = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=10, choices=status_choieces, default='simple')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    colors = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Great_Product(models.Model):
    name = models.ForeignKey(Intorduce, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name