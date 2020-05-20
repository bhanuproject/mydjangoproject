
from django.conf import urls
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    path('registration.html', views.registration, name="registration"),
    url(r'^submit_form_method/$', views.submit_form_method, name="submit_form_method")
]
