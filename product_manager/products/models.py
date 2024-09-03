from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from .models import User

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STOCK_STATUS_CHOICES = [
        ('in_stock', 'In stock'),
        ('out_of_stock', 'Out of stock'),
    ]
    
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_status = models.CharField(max_length=20, choices=STOCK_STATUS_CHOICES)
    main_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    # add extra images like a normal store? 

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['supplier', 'code'], name='unique_product_code')
        ]

    def __str__(self):
        return f"{self.name} ({self.code})"

# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images/')
#     is_main = models.BooleanField(default=False)
    

class User(AbstractUser):
    # Adding related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )


# Buyer group isn't saving through django admin config

# @receiver(post_save, sender=User)
# def add_user_to_buyer_group(sender, instance, created, **kwargs):
#     if created:
#         buyer_group, created = Group.objects.get_or_create(name='Buyer')
#         instance.groups.add(buyer_group)
