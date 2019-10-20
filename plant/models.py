from django.db import models
from django.utils import timezone
from django.utils.deconstruct import deconstructible
from django.urls import reverse
from multiselectfield import MultiSelectField
import uuid
import os

# Global scope variables
TOXICITY_CHOICES = (('dogs', 'Toxic to dogs'),
					('cats', 'Toxic to cats'),
					('humans', 'Toxic to humans'))
# Create your models here.
class Plant(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
	common_name = models.CharField(max_length=100)
	botanical_name = models.CharField(max_length=100)
	alternative_names = models.CharField(max_length=100, null=True)
	sun_requirements = models.TextField(blank=True)
	soil_requirements = models.TextField(blank=True)
	watering_frequency = models.TextField(blank=True)
	fertilizer_frequency = models.TextField(blank=True)
	toxicity = MultiSelectField(choices=TOXICITY_CHOICES)
	profile_picture = models.ImageField(upload_to="plant_pics/", default="default-plant.jpg")
	last_updated = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.common_name

	def get_absolute_url(self):
		return reverse('plant-detail', kwargs={'pk': self.pk})

@deconstructible
class PathAndRename(object):
	def __init__(self, sub_path):
		self.path = sub_path

	def __call__(self, instance, filename):
		ext = filename.split('.')[-1]
		filename = '{}.{}'.format(instance.plant.id, ext)
		return os.path.join(self.path, filename)

path_and_rename = PathAndRename("plant_pics")

class Image(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
	plant = models.ForeignKey(Plant, 
								default=None, 
								on_delete=models.CASCADE)
	image = models.ImageField(upload_to=path_and_rename,
							  verbose_name='Image')
