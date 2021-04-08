from django.urls import path
from .import views

urlpatterns =[
    path('',views.home,name='home'),
    path('about.html',views.about,name='about'),
    path('Registration.html',views.Registration,name='Registration'),
    path('contact.html',views.contact,name='contact'),
]