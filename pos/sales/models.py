from django.db import models
from django.utils import timezone
from product.models import Product

# Create your models here.

class Sales(models.Model):
    
    customer_name = models.CharField(max_length=30)
    grand_total = models.FloatField(default=0)
    date = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
          return self.customer_name
      
class SalesItem(models.Model):
    sales_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)
    def __str__(self):
          return self.sales_id.customer_name