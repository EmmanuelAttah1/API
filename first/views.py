from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # Home page View
    return HttpResponse("<h1>Home Page</h1>")