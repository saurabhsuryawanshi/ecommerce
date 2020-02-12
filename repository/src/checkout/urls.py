from django.urls import path,re_path
from .views import(
	checkout
	)
app_name="checkouts"
urlpatterns=[
	re_path(r"^checkoutdemo/$",checkout,name="checkoutdemo")
]