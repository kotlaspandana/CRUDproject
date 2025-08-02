from django.db import models
class Product(models.Model):
    productid=models.IntegerField()
    productname=models.CharField(max_length=10)
    productprice=models.FloatField()
    productquantity=models.IntegerField()
    def __str__(self):
        return self.productid



