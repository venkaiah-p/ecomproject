from django.urls import path
from myapp.views import index
from myapp.views import customer_details
app_name='myapp'

urlpatterns = [
 path('',index,name='index'),
 path('customer_details/',customer_details,name='customer_details'),
]