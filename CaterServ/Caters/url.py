from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
   path('about/',views.about,name='about'),
   path('service/',views.service,name='about'),
   path('event/',views.event,name='event'),
   path('menu/',views.menu,name='menu'),
   path('book/',views.booking,name='book'),
   path('blog/',views.blog,name='blog'),
   path('teams/',views.team,name='teams'),
   path('testimonial/',views.testimonial,name='testimonial'),
   path('404/',views.page404,name='404'),
   path('contact/',views.contact,name='contact'),
   path('book now/',views.booknow,name='book'),
   
   
]