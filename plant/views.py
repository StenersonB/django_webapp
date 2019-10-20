from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView
from .forms import ImageForm, PlantCreationForm
from .models import Image
from .models import Plant

@login_required
def PlantCreateView(request):

	ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=0)

	if request.method == 'POST':

		plantForm = PlantCreationForm(request.POST, request.FILES)
		#formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

		if plantForm.is_valid():
			plant_form = plantForm.save(commit=False)
			plant_form.save()

			#for form in formset.cleaned_data:
				#Stops from crashing if a user doesn't upload all photos
				#if form:
					#image = form['image']
					#photo = Image(plant=plant_form, image=image)
					#photo.save()
			#else:
				#print(plantForm.errors, formset.errors)
		messages.success(request, plantForm.errors)
		return HttpResponseRedirect("/")
	else:
		plantForm = PlantCreationForm()
		formset = ImageFormSet(queryset=Image.objects.none())
	return render(request, 'plant/new_plant_form.html', {'plantForm': plantForm, 'formset': formset})

class PlantListView(ListView):
	model = Plant
	template_name = 'plant/plant_list.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'plants'

class PlantDetailView(DetailView):
	model = Plant

class PlantUpdateView(LoginRequiredMixin, UpdateView):
	model = Plant
	fields = ['common_name', 'botanical_name', 'alternative_names', 'sun_requirements', 'soil_requirements', 'watering_frequency', 'fertilizer_frequency', 'toxicity']
	template_name_suffix = '_update_form'