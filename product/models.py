from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    def rating_kp(self):
        return 0

    
STARS = ((i, '* ' * i) for i in range(1, 11))
    
class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, default=5)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')



    def __str__(self):
        return f"{self.text}"
    
class UserConfirm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='confirm')
    code = models.CharField(max_length=6)
    
