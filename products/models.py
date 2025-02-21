from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


# Create your models here.
# for image thumbnail
from django.core.files import File
from PIL import Image
from io import BytesIO

class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add =True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = 'Categories'


	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
	post_by = models.ForeignKey(User, related_name='staff', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	slug = models.SlugField()
	description = models.TextField(blank=True, null=True)
	price = models.PositiveIntegerField()
	item_image = models.ImageField(upload_to='products', blank=True, null=True)
	thumbnail = models.ImageField(upload_to='products', blank=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add =True)

	class Meta:
		ordering = ('-created_at',)
		verbose_name_plural = 'Products'


	def __str__(self):
		return self.name

	def get_thumbnail(self):
		if self.thumbnail:
			return self.thumbnail.url
		else:
			if self.item_image:
				self.thumbnail = self.make_thumbnail(self.item_image)
				self.save()

				return self.thumbnail.url
			else:
				return 'https://placehold.co/240x240.jpg'

	def make_thumbnail(self, item_image, size=(400, 400)):
		img = Image.open(item_image)
		img.convert('RGB')
	
		img.thumbnail(size)

		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)
		thumbnail = File(thumb_io, name=item_image.name)

		return thumbnail


	def image_tag(self):
		if self.item_image:
			return mark_safe('<img src="{}" height="50" />'.format(self.item_image.url))
		else: 
			return  mark_safe("<img src='https://placehold.co/240x240.jpg' height='50' />")

	image_tag.short_description = "Item Photo"
