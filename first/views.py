from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def details(request):
    return HttpResponse("Details page")