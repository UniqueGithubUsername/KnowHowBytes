from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=2555, null=True)
	slug = models.SlugField(null=True)
	img = models.ImageField(upload_to="author-img", null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField(max_length=2555, null=True)
	slug = models.SlugField(null=True)
	img = models.ImageField(upload_to="category-img", null=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
	author = models.ForeignKey(Author, models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=255)
	slug = models.SlugField(null=True)
	img = models.ImageField(upload_to="post-img", null=True)
	desc = models.TextField(max_length=2555)
	section = models.CharField(max_length=255, null=True)
	body = models.TextField(max_length=2555)

	section1 = models.CharField(max_length=255, null=True)
	body1 = models.TextField(max_length=2555, null=True)

	section2 = models.CharField(max_length=255, null=True)
	body2 = models.TextField(max_length=2555, null=True)

	section3 = models.CharField(max_length=255, null=True)
	body3 = models.TextField(max_length=2555, null=True)

	postprev = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="prev")
	postnext = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="next")

	def __str__(self):
		return self.title