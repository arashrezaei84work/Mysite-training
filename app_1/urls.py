from django.urls import path
from app_1.views import * 

app_name = 'app_1'

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name='about'),
    path("contact/", contact, name="contact"),
    path('test', test_view, name='test'),
]
