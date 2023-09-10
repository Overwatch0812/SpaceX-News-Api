from .views import apiView,post_data,index
from django.urls import path

urlpatterns = [
    path('',apiView,name="apiview"),
    path('post/',post_data,name="post_data"),
]
