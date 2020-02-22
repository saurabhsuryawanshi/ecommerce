from django.db import models
from products.models import Product
from carts.models import Cart
# Create your models here.
class LineItem(models.Model):
	product_id=models.ForeignKey(Product,models.SET_NULL,blank=True,null=True)
	cart_id=models.ForeignKey(Cart,models.SET_NULL,blank=True,null=True)
	quantity=models.DecimalField(max_digits=120,decimal_places=2,default=0.00)
	total=models.DecimalField(max_digits=120,decimal_places=2,default=0.00)
