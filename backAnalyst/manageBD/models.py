from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Product'
        managed = False

class Changes(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Changes'
        managed = False