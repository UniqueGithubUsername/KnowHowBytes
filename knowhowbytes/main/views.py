from django.shortcuts import render
from .models import Author, Category, Post

# Create your views here.
def home(request):
	authors = Author.objects.all()
	categories = Category.objects.all()
	context = {'authors':authors, 'categories':categories}
	return render(request, 'main/home.html', context)

def category(request, slug):
	categories = Category.objects.all()
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(category=category)
	context = {'categories':categories,'category':category,'posts':posts}
	return render(request, 'main/category.html', context)

def post(request, slug1, slug2):
	categories = Category.objects.all()
	category = Category.objects.get(slug=slug1)
	post = Post.objects.get(slug=slug2)
	context = {'categories':categories,'category':category,'post':post}
	return render(request, 'main/post.html', context)