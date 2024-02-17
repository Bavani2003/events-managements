from django.urls import path
from.import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('decoration/', views.decoration, name='decoration'),
    path('catering/', views.catering,name='catering'),
    path('photoshoot/', views.photoshoot,name='photoshoot'),
    path('booking/', views.booking, name='booking'),
]


