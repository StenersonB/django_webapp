from django import forms
from multiselectfield import MultiSelectField
from .models import Plant, Image

class PlantCreationForm(forms.ModelForm):
	common_name = forms.CharField()
	botanical_name = forms.CharField()
	alternative_names = forms.CharField()
	sun_requirements = forms.Textarea()
	soil_requirements = forms.Textarea()
	watering_frequency = forms.Textarea()
	fertilizer_frequency = forms.Textarea()
	toxicity = MultiSelectField()
	profile_picture = forms.ImageField()

	class Meta:
		model = Plant
		fields = ['common_name', 'botanical_name', 'alternative_names', 'sun_requirements', 'soil_requirements', 'watering_frequency', 'fertilizer_frequency', 'toxicity', 'profile_picture']

class ImageForm(forms.ModelForm):
	image = forms.ImageField(label='Image')
	
	class Meta:
		model = Image
		fields = ['image']
