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
    path('settings', views.settings, name = 'settings'),
    path('layout11', views.layout11, name = 'layout11'),
    path('layout12', views.layout12, name = 'layout12'),
    path('layout13', views.layout13, name = 'layout13'),
    path('layout21', views.layout21, name = 'layout21'),
    path('layout22', views.layout22, name = 'layout22'),
    path('layout23', views.layout23, name = 'layout23'),
    path('layout31', views.layout31, name = 'layout31'),
    path('layout32', views.layout32, name = 'layout32'),
    path('layout33', views.layout33, name = 'layout33'),
    path('layout41', views.layout41, name = 'layout41'),
    path('layout42', views.layout42, name = 'layout42'),
    path('layout43', views.layout43, name = 'layout43')
]