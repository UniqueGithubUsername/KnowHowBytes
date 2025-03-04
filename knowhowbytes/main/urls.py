from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug>', views.category, name='category'),
    path('blog/<slug1>/<slug2>', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('author/<slug>', views.author, name='author')
]