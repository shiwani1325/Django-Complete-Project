from django.urls import path
from ecommapp.views import get_product

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product"),
]