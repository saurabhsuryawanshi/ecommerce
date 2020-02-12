from django.shortcuts import render
from products.models import Product
# Create your views here.
def checkout(request):
	products=Product.objects.all()
	context={
		"products":products
	}
	return render(request,'checkout.html',context)
