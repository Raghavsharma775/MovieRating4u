from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="MovieHome"),
    path('about/',views.index, name="AboutUs"),
    path('contact/',views.contact, name="ContactUs"),
    path('actors/',views.actors, name="ActorsName"),
    path('bollywood/',views.bollywood, name="BollywoodMovie"),
    path('hollywood/',views.hollywood, name="HollywoodMovie"),
    path('movieview/',views.movieview, name="MovieView"),
    path('search/', views.search, name="Moviepage"),
]
