from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_view, name="index"),
    path("detail", blog_detail, name="detail"), # single
    path("test/", test, name="test"),
]
