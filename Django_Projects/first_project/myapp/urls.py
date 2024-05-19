from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name ='index'),
    path('about', views.aboutme,name = 'aboutme'),
    path('Women.html', views.Women,name = 'Women'),
    path('art.html', views.art,name = 'art'),
]
