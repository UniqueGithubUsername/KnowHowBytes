from django.shortcuts import render
from .models import Author, Category, Post

# Create your views here.
def home(request):
	authors = Author.objects.all()
	print(authors)
	categories = Category.objects.all()
	context = {'authors':authors, 'categories':categories}
	return render(request, 'main/home.html', context)

def blog(request):
	categories = Category.objects.all()
	posts = Post.objects.all()
	context = {'categories':categories,'posts':posts}
	return render(request, 'main/blog.html', context)

def category(request, slug):
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(category=category)
	context = {'category':category,'posts':posts}
	return render(request, 'main/category.html', context)

def post(request, slug1, slug2):
	category = Category.objects.get(slug=slug1)
	post = Post.objects.get(slug=slug2)
	posts = Post.objects.filter(category=category).exclude(id=post.id)
	post_sections = post.get_sections()
	context = {'category':category,'posts':posts,'post':post,'post_sections':post_sections}
	return render(request, 'main/post.html', context)

def about(request):
	authors = Author.objects.all()
	categories = Category.objects.all()
	context = {'authors':authors, 'categories':categories}
	return render(request, 'main/about.html', context)