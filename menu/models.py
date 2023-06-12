from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Menu(models.Model):
    """"""
    title = models.TextField(max_length=250, blank=False)
    description = models.TextField(max_length=500, blank=True)
    weight = models.IntegerField(blank=True, validators=[MinValueValidator(1)])
    price = models.IntegerField(blank=False, validators=[MinValueValidator(1)])
    discount_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)])
    photo_url = models.ImageField(upload_to='images')
    add_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.title


