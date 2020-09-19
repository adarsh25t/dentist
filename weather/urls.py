from django.urls import path

from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about.html', views.about, name='about'),
   path('contact.html', views.contact, name='contact'),
   path('pricing.html', views.pricing, name='pricing'),
   path('service.html', views.service, name='service'),
   path('blog.html', views.blog, name='blog'),
   path('blog-details.html', views.bdetails, name='bdetails'),
   path('book.html', views.book, name='book')
]