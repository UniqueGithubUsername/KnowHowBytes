from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<slug>', views.category, name='category'),
    path('<slug1>/<slug2>', views.post, name='post')
]