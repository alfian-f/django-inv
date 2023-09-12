from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
    price = models.IntegerField()