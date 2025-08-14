from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def about(request):
    return render(request, "app_1/about.html")

def contact(request):
    return render(request, "app_1/contact.html")