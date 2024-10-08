from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug>', views.category, name='category'),
    path('<slug1>/<slug2>', views.post, name='post')
]