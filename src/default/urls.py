from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('elements-path/', views.elements_path, name='elements-path'),
]