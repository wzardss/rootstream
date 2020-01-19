from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def signup(request):
    return render(request, 'dashboard/signup.html')

def about(request):
    return render(request, 'dashboard/about.html')

def contact(request):
    return render(request, 'dashboard/contact.html')