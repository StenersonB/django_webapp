from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	POST_TYPES = (
	('General Question', 'General Question'),
	('Identity Request', 'Identity Request'),
	('Troubleshoot Request', 'Troubleshoot Request'),
	)
	title = models.CharField(max_length=100)
	post_type = models.CharField(max_length=50, choices=POST_TYPES, default='General Question')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def get_image_filename(instance, filename):
		return instance.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

class Image(models.Model):
	post = models.ForeignKey(Post, 
								default=None, 
								on_delete=models.CASCADE)
	image = models.ImageField(upload_to='post_pics', 
							  verbose_name='Image')