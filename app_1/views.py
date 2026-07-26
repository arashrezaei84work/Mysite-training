from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from app_1.forms import ContactForm, NewsLetterForm

# Create your views here.

def index(request):
    return render(request, "app_1/index.html")

def about(request):
    return render(request, "app_1/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()             
    return render(request, "app_1/contact.html",{'form':form})


def test_view(request):
    return render(request, "app_1/test.html")

def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return   HttpResponseRedirect('/')
    