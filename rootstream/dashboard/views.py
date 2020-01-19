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

def account(request):
    return render(request, 'dashboard/account.html')

def layout(request):
    return render(request, 'dashboard/layout.html')

def settings(request):
    return render(request, 'dashboard/settings.html')

def layout11(request):
    return render(request, 'dashboard/layout11.html')