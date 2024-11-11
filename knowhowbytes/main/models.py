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
	desc = models.TextField(max_length=255)
	body = models.TextField(max_length=2555)

	postprev = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="prev")
	postnext = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="next")

	def get_sections(self):
		sections = self.body.split("\r\n\r\n\r\n")
		return sections

	def get(section):
		print(section[0])
		return section

	def __str__(self):
		return self.title