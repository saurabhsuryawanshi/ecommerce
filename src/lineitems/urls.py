from django.urls import path,re_path
from .views import (
		create_line_item,
	)
app_name="lineitems"
urlpatterns = [
		path('<id>/',create_line_item,name='create'),
		# path('delete/',delete_line_item,name='delete')
	]

