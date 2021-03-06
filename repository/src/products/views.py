from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product
from carts.models import Cart
from django.http import Http404
# Create your views here.

class ProductFeaturedListView(ListView):
	template_name = "products/list.html"
	def get_queryset(self):
		request=self.request
		return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"
	queryset=Product.objects.filter(featured=True)
	
class ProductDetailSlugView(DetailView):
	queryset=Product.objects.all()
	template_name = "products/detail.html"	

	def get_context_data(self,*args,**kwargs):
		context = super().get_context_data(*args,**kwargs)
		print(super().get_context_data(*args,**kwargs))
		cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		context['cart']=cart_obj
		return context

	def get_object(self,*args,**kwargs):
		request=self.request
		print(self.kwargs,"hey")
		slug=self.kwargs.get('slug')
		# instance=get_object_or_404(Product,slug=slug,active=True)
		try:
			instance=Product.objects.get(slug=slug,active=True)
		except Product.DoesNotExist:
			raise Http404("Not Found..")
		except Product.MultipleObjectsReturned:
			qs=Product.objects.filter(slug=slug,active=True)
			instance=qs.first()
		except:
			raise Http404('uhmmmmm')
		return instance

class ProductListView(ListView):
	template_name = "products/list.html"
	def get_queryset(self):
		request=self.request
		return Product.objects.all()
	# def get_context_data(self,*args,**kwargs):
	# 	context=super(ProductListView, self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context

def product_list_view(request):
	queryset = Product.objects.all()
	context={
		'object_list':queryset
	}
	return render(request,"products/list.html",context)

class ProductDetailView(DetailView):
	template_name = "products/detail.html"
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(**kwargs)
		return kwargs
	
		# queryset=Product.objects.get_by_id(id=pk)

	def get_object(self,*args,**kwargs):
	 	request=self.request
	 	pk=self.kwargs.get('pk')
	 	instance=Product.objects.get_by_id(id=pk)
	 	if instance is None:
	 		raise Http404("product doesn't exists")
	 	return instance

def product_detail_view(request,pk=None,*args,**kwargs):
	# instance = Product.objects.get(pk=pk)
	#instance=get_object_or_404(Product,id=pk)*
	# try:
	# 	instance=Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print("no product here")
	# 	raise Http404("product doesn't exists")
	# except:
	# 	print("huh?")
	instance=Product.objects.get_by_id(id=pk)
	if instance is None:
		raise Http404("product doesn't exists")
	# print(instance)
	# qs=Product.objects.filter(id=pk)
	# #print(qs)
	# if qs.exists() and qs.count()==1:
	# 	instance=qs.first()
	# else:
	# 	raise Http404("Product doesn't exists")
	context={
		'object':instance
	}
	return render(request,"products/detail.html",context)
