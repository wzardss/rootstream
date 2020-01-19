from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signup', views.signup, name='signup'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('account', views.account, name = 'account'),
    path('layout', views.layout, name = 'layout'),
    path('settings', views.layout, name = 'settings')
]