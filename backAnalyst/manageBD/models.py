from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()

    class Meta:
        db_table = 'Product'
        managed = False

class Notification(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Notification'
        managed = False