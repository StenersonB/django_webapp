from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class Post(models.Model):
	POST_TYPES = (
	('Rescue my plant', 'Rescue my plant'),
	('Identify my plant', 'Identify my plant'),
	('General Question', 'General Question'),
	)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=100)
	post_type = models.CharField(max_length=50, choices=POST_TYPES, default='General Question')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def get_first_image(self):
		images = Image.objects.filter(post=self)[0]
		url = images.image
		return url

class Image(models.Model):
	post = models.ForeignKey(Post, 
								default=None, 
								on_delete=models.CASCADE)
	image = models.ImageField(upload_to='post_pics', 
							  verbose_name='Image')