from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_view, name="index"),
    path("category/<str:cat>", blog_view, name="category"), 
    path("author/<str:author_name>", blog_view, name="author"), 
    path("tags/<str:tag_name>", blog_view, name="tag"), 
    path("<int:pid>", blog_detail, name="detail"), # single
    path('search/',blog_search,name='search'),
    # path("test/", test, name="test"),
]
