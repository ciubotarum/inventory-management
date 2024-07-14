from django.db import models

# Create your models here.
# Setup database to store products with different id numbers
class Product(models.Model):
    # primary_key is a unique identifier assigned to each record in the database
    product_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        