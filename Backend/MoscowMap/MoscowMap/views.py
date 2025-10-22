from django.shortcuts import render, HttpResponse

def home(request):
    
    return HttpResponse("<h1>Здесь будет карта</h1>")
