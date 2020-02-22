"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,re_path,include
from accounts.views import login_page,register_page,LogoutView,guest_register_view
from .views import home_page,about_page,contact_page,home_page_old
from django.views.generic import TemplateView
from carts.views import cart_home
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
# from lineitems.views import create_line_item
# from products.views import (
# 	ProductListView,
# 	product_list_view,
# 	ProductDetailView,
# 	product_detail_view,
# 	ProductFeaturedListView,
# 	ProductFeaturedDetailView,
# 	ProductDetailSlugView
# 	)
urlpatterns = [
	re_path(r'^$',home_page,name='home'),
	re_path(r'^about/$',about_page,name='about'),
	re_path(r'^contact/$',contact_page,name='contact'),
	re_path(r'^login/$',login_page,name='login'),
	re_path(r'^register/guest/$',guest_register_view,name='guest_register'),
	re_path(r'^logout/$',LogoutView.as_view(),name='logout'),
	re_path(r'^register/$',register_page,name='register'),
	re_path(r'^checkout/address/create/$',checkout_address_create_view,name='checkout_address_create'),
	re_path(r'^checkout/address/reuse/$',checkout_address_reuse_view,name='checkout_address_reuse'),
	re_path(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/example.html')),
	re_path(r'products/',include("products.urls",namespace="product")), 
	re_path(r'search/',include("search.urls",namespace="search")), 
	re_path(r'carts/',include("carts.urls",namespace="carts")),
	re_path(r'lineitems/',include("lineitems.urls",namespace="lineitems")),
	re_path(r'checkouts/',include("checkout.urls",namespace="checkouts")),
	path('heythere/',home_page_old,name="jhonny"),
	# re_path(r'^products/$',ProductListView.as_view()), 
	# re_path(r'^featured/$',ProductFeaturedListView.as_view()),
	# re_path(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
	# re_path(r'^products-fbv/$',product_list_view),
	# re_path(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view), 
	# re_path(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
	# re_path(r'^products/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()), 
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
	urlpatterns=urlpatterns+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
	