from django.shortcuts import render
from .models import LineItem
from products.models import Product
from carts.models import Cart
import math

def create_line_item(request,*args,**kwargs):	
	a=kwargs['id']
	product_id=float(kwargs["id"].split('-')[0])
	product=Product.objects.get(id=product_id)
	price=float(kwargs["id"].split('-')[1])
	a=isinstance(product_id,float)
	b=isinstance(price,float)
	print(a,b)
	cart_id=request.session['cart_id']
	cart=Cart.objects.get(id=cart_id)
	lineitem,created=LineItem.objects.get_or_create(product_id=product,cart_id=cart)
	lineitem.total=math.fsum([lineitem.total,price])
	lineitem.quantity=math.fsum([lineitem.quantity,1])	
	lineitem.save()
	return render(request,'checkout.html',{})
	