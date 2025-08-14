from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")