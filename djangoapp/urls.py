from django.urls import path

from djangoapp import views



urlpatterns = [
    path('', views.home, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('services/', views.testimonial, name='my_testimonial'),
    path('contact/', views.contact, name='my_contact'),
    path('property_list/', views.property_list, name='my_property_list'),
    path('property_type/', views.property_type, name='my_property_type'),
    path('property_agent/', views.property_agent, name='my_property_agent'),
    path('my_404/', views.my_404, name='my_404'),
]