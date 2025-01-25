
from django.urls import path
from . import views
from .views import contact
urlpatterns = [
  path('',views.home, name="home"),
  path('contact.html',views.contact, name="contact"),
  path('about.html',views.about, name="about"),
  path('service.html',views.service, name="service"),
  path('price.html',views.price, name="price"),
  path('appointment.html',views.appointment, name="appointment")
]


