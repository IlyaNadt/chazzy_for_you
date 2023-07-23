from django.shortcuts import render

def HomePageView(request):
    return render(request, "base/home.html")

def AboutPageView(request):
    return render(request, 'base/contacts.html')
