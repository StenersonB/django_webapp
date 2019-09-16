from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Plant(models.Model):
	common_name = models.CharField(max_length=100)
	botanical_name = models.CharField(max_length=100)
	alternative_names = models.CharField(max_length=100, null=True)
	sun_requirements = models.TextField(blank=True)
	soil_requirements = models.TextField(blank=True)
	watering_frequency = models.TextField(blank=True)
	fertilizer_frequency = models.TextField(blank=True)
	toxicity = models.TextField(blank=True)
	last_updated = models.DateTimeField(default=timezone.now)

	def get_image_filename(instance, filename):
		common_name = instance.plant.common_name
		slug = slugify(common_name)
		return "plant_pics/%s-%s" % (slug, filename)

	def __str__(self):
		return self.common_name

class Image(models.Model):
	plant = models.ForeignKey(Plant, 
								default=None, 
								on_delete=models.CASCADE)
	image = models.ImageField(upload_to='plant_pics',
							  verbose_name='Image')
