from django.http import HttpResponse, JsonResponse

def default(request):
    return HttpResponse("<h1>This is index page!</h1>")